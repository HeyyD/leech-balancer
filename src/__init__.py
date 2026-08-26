import anki.cards
import aqt.reviewer

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QDialog, QHBoxLayout, QLabel, QGridLayout, QDialogButtonBox, QVBoxLayout, QSpinBox, QCheckBox, QComboBox, QProgressBar
from aqt import utils, mw, qconnect
from aqt.gui_hooks import reviewer_did_answer_card

CONFIG_REQUIRED_CORRECT_ANSWERS = 'required_correct_answers'
CONFIG_SHOW_TOAST = 'show_toast'

def get_config():
    return mw.addonManager.getConfig(__name__)

def get_last_correct_answers(answers):
    result = []
    for element in answers:
        if element > 1:
            result.append(element)
        else:
            break
    return result

def get_answers(card: anki.cards.Card):
    cmd = f'SELECT ease FROM revlog WHERE cid IS {card.id} ORDER BY id DESC'
    return card.col.db.list(cmd)

def was_consecutively_correct(correct_answers, times: int):
    total_consecutively_correct = len(correct_answers)
    return total_consecutively_correct >= times and total_consecutively_correct % times == 0

def on_answer(context: aqt.reviewer.Reviewer, card: anki.cards.Card, ease: int):
    answers = get_answers(card)
    correct_answers = get_last_correct_answers(answers)
    updated_card = card.col.get_card(card.id)
    if was_consecutively_correct(correct_answers, 3) and updated_card.lapses > 0:
        updated_card.lapses -= 1
        context.mw.col.update_card(updated_card)
        context.mw.col.update_note(updated_card.note())
        utils.tooltip(f'Answered correct {len(correct_answers)} times in a row. Reduced lapse of the card.', period=3000)

def open_setting_dialogue():
    config = get_config()

    dialog = QDialog(mw)
    dialog.setWindowTitle("Leech Balancer")

    grid = QGridLayout()

    show_toast_label = QLabel("Show toast")
    show_toast = QCheckBox()
    show_toast.setChecked(config.get(CONFIG_SHOW_TOAST, True))
    grid.addWidget(show_toast_label, 0, 0)
    grid.addWidget(show_toast, 0, 1)

    required_correct_answers_label = QLabel("Required correct answers")
    required_correct_answers = QSpinBox()
    required_correct_answers.setMinimumWidth(200)
    required_correct_answers.setValue(config.get(CONFIG_REQUIRED_CORRECT_ANSWERS, 3))

    grid.addWidget(required_correct_answers_label, 1, 0)
    grid.addWidget(required_correct_answers, 1, 1)

    def save_config():
        config[CONFIG_REQUIRED_CORRECT_ANSWERS] = required_correct_answers.value()
        config[CONFIG_SHOW_TOAST] = show_toast.isChecked()
        mw.addonManager.writeConfig(__name__, config)
        dialog.close()

    ok = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
    ok.clicked.connect(save_config)

    cancel = QDialogButtonBox(QDialogButtonBox.StandardButton.Cancel)
    cancel.clicked.connect(dialog.close)

    buttons_layout = QHBoxLayout()
    buttons_layout.addStretch(1)
    buttons_layout.addWidget(ok)
    buttons_layout.addWidget(cancel)

    layout = QVBoxLayout()
    layout.addLayout(grid)
    layout.addLayout(buttons_layout)

    dialog.setLayout(layout)
    dialog.exec()

def init_menu():
    configs = QAction("Leech Balancer Config", mw)
    qconnect(configs.triggered, open_setting_dialogue)
    mw.form.menuTools.addAction(configs)


def init():
    print('Setting up lapse reducer....')
    reviewer_did_answer_card.append(on_answer)
    init_menu()
