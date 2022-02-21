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
        vocational_test = models.BooleanField(
        choices=[
                [False, 'no-test'],
                [True, 'test'],
            ]
        )       



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField(blank=True)
    consent_account = models.BooleanField(blank=True)
    identificador = models.StringField(label='Para iniciar por favor ingrese las iniciales de su primer nombre y apellido seguido de su fecha de nacimiento. Por ejemplo, si usted se llama Lina Ríos y usted nació el 11 de febrero de 1995, debe ingresar LR11021995. Escriba todo en mayúscula. Este código es importante para asegurar su participación en el resto de la actividad y la realización de los pagos.')

