import anki.cards
import aqt.reviewer

from aqt import mw, utils
from aqt.gui_hooks import reviewer_did_answer_card

from .config import CONFIG_REQUIRED_CORRECT_ANSWERS, CONFIG_SHOW_TOAST

def get_config_value(key, default):
    return mw.addonManager.getConfig(__name__).get(key, default)

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
    required_correct_answers = get_config_value(CONFIG_REQUIRED_CORRECT_ANSWERS, 3)
    show_toast = get_config_value(CONFIG_SHOW_TOAST, True)

    answers = get_answers(card)
    correct_answers = get_last_correct_answers(answers)
    updated_card = card.col.get_card(card.id)
    if was_consecutively_correct(correct_answers, required_correct_answers) and updated_card.lapses > 0:
        undo = context.mw.col.undo_status().last_step
        updated_card.lapses -= 1
        context.mw.col.update_card(updated_card)
        context.mw.col.update_note(updated_card.note())
        context.mw.col.merge_undo_entries(undo)
        print('Reduced lapse of the card.')
        if show_toast:
            utils.tooltip(f'Answered correct {len(correct_answers)} times in a row. Reduced lapse of the card.', period=3000)


def init():
    print('Setting up lapse reducer....')
    reviewer_did_answer_card.append(on_answer)
