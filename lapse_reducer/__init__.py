import anki.cards
import aqt.reviewer

from aqt import utils
from aqt.gui_hooks import reviewer_did_answer_card

def get_last_correct_answers(answers):
    result = []
    for element in answers:
        if element > 1:
            result.append(element)
        else:
            break
    return result

def was_consecutively_correct(card: anki.cards.Card, times: int):
    cmd = f'SELECT ease FROM revlog WHERE cid IS {card.id} ORDER BY id DESC'
    answers = card.col.db.list(cmd)
    total_consecutively_correct = len(get_last_correct_answers(answers))

    return total_consecutively_correct >= times and total_consecutively_correct % times == 0

def on_answer(context: aqt.reviewer.Reviewer, card: anki.cards.Card, ease: int):
    updated_card = card.col.get_card(card.id)
    if was_consecutively_correct(card, 3) and updated_card.lapses > 0:
        updated_card.lapses -= 1
        context.mw.col.update_card(updated_card)
        context.mw.col.update_note(updated_card.note())
        utils.tooltip('Reduced lapse of the card', period=3000)

def init():
    print('Setting up lapse reducer....')
    reviewer_did_answer_card.append(on_answer)
