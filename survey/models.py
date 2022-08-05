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
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    job2_1 = models.StringField()
    job2_2 = models.StringField()
    job2_3 = models.StringField()
    job2_4 = models.StringField()
    job2_5 = models.StringField()

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

    puntaje_global = models.IntegerField();

    educ_type = models.IntegerField(
    choices=[
        [1,'Técnica'],
        [2,'Tecnológica'],
        [3,'Profesional'],
        [4,'Ninguna']
    ], label="¿Para hacer lo que más le gusta es necesaria una carrera?")

    educ_university = models.StringField(label="Escriba el nombre de la institución en la que desea estudiar:")