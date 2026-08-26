import anki.cards
import aqt.reviewer

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QDialog, QHBoxLayout, QLabel, QLineEdit, QDialogButtonBox, QVBoxLayout, QSpinBox, QCheckBox, QComboBox, QProgressBar
from aqt import utils, mw, qconnect
from aqt.gui_hooks import reviewer_did_answer_card

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

def setting_dialogue():
    dialog = QDialog(mw)
    dialog.setWindowTitle("Leech Balancer")

    required_correct_answers_layout = QHBoxLayout()
    required_correct_answers_label = QLabel("Required correct answers:")
    required_correct_answers_def = QSpinBox()
    required_correct_answers_def.setMinimumWidth(200)
    required_correct_answers_layout.addWidget(required_correct_answers_label)
    required_correct_answers_layout.addWidget(required_correct_answers_def)

    ok = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
    cancel = QDialogButtonBox(QDialogButtonBox.StandardButton.Cancel)
    buttons_layout = QHBoxLayout()
    buttons_layout.addStretch(1)
    buttons_layout.addWidget(ok)
    buttons_layout.addWidget(cancel)

    layout = QVBoxLayout()
    dialog.setLayout(layout)
    layout.addLayout(required_correct_answers_layout)
    layout.addLayout(buttons_layout)

    dialog.exec()

def init_menu():
    configs = QAction("Leech Balancer Config", mw)
    qconnect(configs.triggered, setting_dialogue)
    mw.form.menuTools.addAction(configs)


def init():
    print('Setting up lapse reducer....')
    reviewer_did_answer_card.append(on_answer)
    init_menu()
