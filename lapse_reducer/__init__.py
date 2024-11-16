import anki.cards
import aqt.reviewer

from aqt import utils
from aqt.gui_hooks import reviewer_did_answer_card

def get_last_correct_answers(answers):
    result = []
    for element in reversed(answers):
        if element > 1:
            result.append(element)
        else:
            break
    return result

def was_consecutively_correct(card: anki.cards.Card, times: int):
    cmd = f'SELECT ease FROM revlog WHERE cid IS {card.id} ORDER BY id DESC'
    answers = card.col.db.list(cmd)
    total_consecutively_correct = len(get_last_correct_answers(answers))

    return total_consecutively_correct >= times


def on_answer(context: aqt.reviewer.Reviewer, card: anki.cards.Card, ease: int):
    updated_card = card.col.get_card(card.id)
    if was_consecutively_correct(card, 1) and updated_card.lapses > 0:
        updated_card.lapses -= 1
        utils.tooltip('Reduced lapse of the card', period=3000)

def init():
    reviewer_did_answer_card.append(on_answer)
    print('Setting up lapse reducer....')
