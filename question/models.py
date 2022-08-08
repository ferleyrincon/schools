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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'question'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    test_job1 = models.StringField()
    test_job2 = models.StringField()
    test_job3 = models.StringField()
    test_job4 = models.StringField()
    test_job5 = models.StringField()

    job2_1 = models.StringField()
    job2_2 = models.StringField()
    job2_3 = models.StringField()
    job2_4 = models.StringField()
    job2_5 = models.StringField()
