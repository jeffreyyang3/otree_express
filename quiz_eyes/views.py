from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class eyes_instructions(Page):
    form_model = models.Player
    form_fields = ['time_eyes_instructions']
    def is_displayed(self):
        return self.round_number == 1

class Question(Page):
    form_model = models.Player
    form_fields = ['submitted_answer', 'time_Question']

    def submitted_answer_choices(self):
        qd = self.player.current_question()
        return [
            qd['choice1'],
            qd['choice2'],
            qd['choice3'],
            qd['choice4'],
        ]

    def before_next_page(self):
        self.player.check_correct()


    def vars_for_template(self):
        return {
            'image_path': 'quiz_eyes/pics/q{}.png'.format(
                self.round_number),
        }

class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        player_in_all_rounds = self.player.in_all_rounds()
        return {
            'player_in_all_rounds': player_in_all_rounds,
            'questions_correct': sum([p.is_correct for p in player_in_all_rounds]),
            'individual_score': str(round(sum([p.is_correct for p in player_in_all_rounds])/36, 2)*100)[:2]+'%'
        }


page_sequence = [
    eyes_instructions,
    Question,
    Results
]
