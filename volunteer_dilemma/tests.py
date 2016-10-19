# -*- coding: utf-8 -*-
from __future__ import division

import random

from otree.common import Currency as c, currency_range

from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    cases = ['0_volunteer', '1_volunteer']

    def play_round(self):
        case = self.case

        yield (views.Introduction)

        if case == '0_volunteer':
            yield (views.Decision, {'volunteer': False})
            assert self.player.payoff == c(0)
            assert 'You did not volunteer and no one did' in self.html
        elif case == '1_volunteer':
            yield (views.Decision, {'volunteer': self.player.id_in_group == 1})
            if self.player.id_in_group == 1:
                assert 'You volunteered' in self.html
                assert self.player.payoff == Constants.general_benefit - Constants.volunteer_cost
            else:
                assert 'You did not volunteer but some did' in self.html
                assert self.player.payoff == c(100)
        yield (views.Results)