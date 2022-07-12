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


class Subsession(BaseSubsession):
    pass



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField(blank=True)
    consent_account = models.BooleanField(blank=True)

    mi_mundo1 = models.StringField()
    mi_mundo2 = models.StringField()
    mi_mundo3 = models.StringField()
    mi_mundo4 = models.StringField()
    mundo_trabajo1 = models.StringField()
    mundo_trabajo2 = models.StringField()
    mundo_trabajo3 = models.StringField()
    mundo_trabajo4 = models.StringField()
    mundo_trabajo5 = models.StringField()
    mundo_trabajo6 = models.StringField()
    mundo_trabajo7 = models.StringField()
    mundo_trabajo8 = models.StringField()
    mundo_trabajo9 = models.StringField()
    mundo_trabajo10 = models.StringField()
    mundo_trabajo11 = models.StringField()
    mundo_trabajo12 = models.StringField()
    mundo_trabajo13 = models.StringField()
    mundo_formacion1 = models.StringField()
    mundo_formacion2 = models.StringField()
    mundo_formacion3 = models.StringField()
    mundo_formacion4 = models.StringField()
    mundo_formacion5 = models.StringField()
    mundo_formacion6 = models.StringField()
    mundo_formacion7 = models.StringField()

    prueba_20000 = models.StringField();
    prueba_15000 = models.StringField();
    prueba_10000 = models.StringField();
    prueba_5000 = models.StringField();

    puntaje_20000 = models.IntegerField();
    puntaje_15000 = models.IntegerField();
    puntaje_10000 = models.IntegerField();
    puntaje_5000 = models.IntegerField();

    prefer_20000 = models.IntegerField();
    prefer_15000 = models.IntegerField();
    prefer_10000 = models.IntegerField();
    prefer_5000 = models.IntegerField();
