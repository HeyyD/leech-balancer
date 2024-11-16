import anki.cards
import aqt.reviewer

from aqt.gui_hooks import reviewer_did_answer_card

def on_answer(context: aqt.reviewer.Reviewer, card: anki.cards.Card, ease: int):
    print('User answered card')

def init():
    reviewer_did_answer_card.append(on_answer)
    print('Setting up lapse reducer....')
