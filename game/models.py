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

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'game'
    players_per_group = None
    num_rounds = 1
    profitability = {
        1: {
            1: {'i1':   10,     'i2': 10},
            2: {'i1':   10,     'i2': 10},
            3: {'i1':   10,     'i2': 10},
            4: {'i1':   6,      'i2': 10},
            5: {'i1':   6,      'i2': 4},
            6: {'i1':   6,      'i2': 4}
        },
        2: {
            1: {'i1':   10,     'i2': 12},
            2: {'i1':   10,     'i2': 12},
            3: {'i1':   6,      'i2': 12},
            4: {'i1':   6,      'i2': 4},
            5: {'i1':   6,      'i2': 4},
            6: {'i1':   10,     'i2': 4}
        },
        3: {
            1: {'i1':   10,     'i2': 10},
            2: {'i1':   10,     'i2': 10},
            3: {'i1':   6,      'i2': 10},
            4: {'i1':   6,      'i2': 10},
            5: {'i1':   6,      'i2': 4},
            6: {'i1':   10,     'i2': 4}
        },
        4: {
            1: {'i1':   10,     'i2': 12},
            2: {'i1':   6,      'i2': 12},
            3: {'i1':   6,      'i2': 12},
            4: {'i1':   6,      'i2': 4},
            5: {'i1':   10,     'i2': 4},
            6: {'i1':   10,     'i2': 4}
        },
        5: {
            1: {'i1':   10,     'i2': 10},
            2: {'i1':   6,      'i2': 10},
            3: {'i1':   6,      'i2': 10},
            4: {'i1':   6,      'i2': 10},
            5: {'i1':   10,     'i2': 4},
            6: {'i1':   10,     'i2': 4}
        },
        6: {
            1: {'i1':   10,     'i2': 12},
            2: {'i1':   10,     'i2': 12},
            3: {'i1':   10,     'i2': 12},
            4: {'i1':   6,      'i2': 4},
            5: {'i1':   6,      'i2': 4},
            6: {'i1':   6,      'i2': 4}
        },
    }


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for j in self.get_players():
                j.get_investment1()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    investment1 = models.BooleanField()  #i1 o i2

    # Problema 1
    ## Asignacion que hace el jugador
    p1_a1   =   models.IntegerField();
    p1_a2   =   models.IntegerField();
    ## Rentabilidad
    p1_r1   =   models.IntegerField();
    p1_r2   =   models.IntegerField();
    ## Pago
    p1_p    =   models.IntegerField();

    # Problema 2
    ## Asignacion que hace el jugador
    p2_a1   =   models.IntegerField();
    p2_a2   =   models.IntegerField();
    ## Rentabilidad
    p2_r1   =   models.IntegerField();
    p2_r2   =   models.IntegerField();
    ## Pago
    p2_p    =   models.IntegerField();

    # Problema 3
    ## Asignacion que hace el jugador
    p3_a1   =   models.IntegerField();
    p3_a2   =   models.IntegerField();
    ## Rentabilidad
    p3_r1   =   models.IntegerField();
    p3_r2   =   models.IntegerField();
    ## Pago
    p3_p    =   models.IntegerField();

    # Problema 4
    ## Asignacion que hace el jugador
    p4_a1   =   models.IntegerField();
    p4_a2   =   models.IntegerField();
    ## Rentabilidad
    p4_r1   =   models.IntegerField();
    p4_r2   =   models.IntegerField();
    ## Pago
    p4_p    =   models.IntegerField();

    # Problema 5
    ## Asignacion que hace el jugador
    p5_a1   =   models.IntegerField();
    p5_a2   =   models.IntegerField();
    ## Rentabilidad
    p5_r1   =   models.IntegerField();
    p5_r2   =   models.IntegerField();
    ## Pago
    p5_p    =   models.IntegerField();

    # Problema 6
    ## Asignacion que hace el jugador
    p6_a1   =   models.IntegerField();
    p6_a2   =   models.IntegerField();
    ## Rentabilidad
    p6_r1   =   models.IntegerField();
    p6_r2   =   models.IntegerField();
    ## Pago
    p6_p    =   models.IntegerField();

    quiz1_1 = models.IntegerField(blank=9, min=0, max=20000, label="Cuánto será su ganancia adicional:")
    quiz1_2 = models.IntegerField(blank=9, min=0, max=20000, label="Cuánto será su ganancia adicional:")
    quiz2   = models.IntegerField(blank=9, min=0, max=20000, label="Cuánto será su ganancia adicional:")

    def get_investment1(self):
        self.investment1 =random.choice([True, False])
        self.participant.vars['investment1'] =self.investment1
        return self.investment1




