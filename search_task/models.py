from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, safe_json
)

import logging

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'search_task'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    debug_mode = models.BooleanField()

    def before_session_starts(self):
        self.debug_mode = self.session.config['debug']
        for person in self.get_players():
            if 'targetIncome' in self.session.config:
                if len(self.session.config['targetIncome']) == len(self.get_players()):
                    person.target_income = self.session.config['targetIncome'][person.id_in_group - 1]
                elif len(self.session.config['targetIncome']) == 1:
                    person.target_income = self.session.config['targetIncome'][0]
                else:
                    assert False, 'targetIncome is not set properly'
            else:
                person.target_income = 10  # default value
            if 'maxScreens' in self.session.config:
                person.maxScreens = self.session.config['maxScreens']
            else:
                person.maxScreens = 20
            if 'screenTime' in self.session.config:
                person.screenTime = self.session.config['screenTime']
            else:
                person.screenTime = 20
            if 'pointDistMin' in self.session.config:
                person.pointDistMin = self.session.config['pointDistMin']
            else:
                person.pointDistMin = 20
            if 'pointDistMax' in self.session.config:
                person.pointDistMax = self.session.config['pointDistMax']
            else:
                person.pointDistMax = 100


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    maxScreens = models.DecimalField(max_digits=5, decimal_places=2)
    screenTime = models.DecimalField(max_digits=5, decimal_places=2)
    pointDistMin = models.DecimalField(max_digits=5, decimal_places=2)
    pointDistMax = models.DecimalField(max_digits=5, decimal_places=2)

    task_reward = models.DecimalField(max_digits=5, decimal_places=2)
    target_income = models.DecimalField(max_digits=5, decimal_places=2)
    # add timestamps
    time_GameInstructions = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_PracticeTask = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_SearchTask = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))


# roles
def role(self):
    if self.id_in_group == 1:
        return 'A'
    if self.id_in_group == 2:
        return 'B'


# gets the id of partner if you are matched, and of him/herself if the player is the reader
def get_partner(self):
    if self.role() == 'A' or self.role() == 'B':
        return self.get_others_in_group()[0]
