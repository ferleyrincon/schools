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

    area_1 = models.StringField();
    area_2 = models.StringField();
    area_3 = models.StringField();
    area_4 = models.StringField();
    area_5 = models.StringField();
    time_init_area = models.FloatField();
    time_area_1 = models.FloatField();
    time_area_2 = models.FloatField();
    time_area_3 = models.FloatField();
    time_area_4 = models.FloatField();
    time_area_5 = models.FloatField();

    occupation_1 = models.StringField();
    occupation_2 = models.StringField();
    occupation_3 = models.StringField();
    time_init_occupation = models.FloatField();
    time_occupation_1 = models.FloatField();
    time_occupation_2 = models.FloatField();
    time_occupation_3 = models.FloatField();
