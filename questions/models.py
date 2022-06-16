from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import numpy as np
import random
import json


author = 'Ferley Rincón'

doc = """
The effect of a vocational test on standardized tests scores: a field experiment.
"""


class Constants(BaseConstants):
    name_in_url = 'schools'
    players_per_group = None
    num_rounds = 1
    fixed_payoff = c(10000)
    task_payoff = random.randint(1,3)


class Subsession(BaseSubsession):
    pass



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField(blank=True)
    consent_account = models.BooleanField(blank=True)

