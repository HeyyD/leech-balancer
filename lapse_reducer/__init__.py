import anki.cards
import aqt.reviewer

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
    value = was_consecutively_correct(card, 2)
    print(value)
    print('User answered card')

def init():
    reviewer_did_answer_card.append(on_answer)
    print('Setting up lapse reducer....')
