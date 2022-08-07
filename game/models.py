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
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Problema 1
    ## Asignacion que hace el jugador
    p1_a1   =   models.IntegerField();
    p1_a2   =   models.IntegerField();
    ## Rentabilidad
    p1_r1   =   models.IntegerField();
    p1_r2   =   models.IntegerField();
    ## Pago
    p1_p    =   models.IntegerField();

