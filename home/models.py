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
    name_in_url = 'home'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def set_id_players(self):
        for j in self.get_players():
            j.set_id()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField(blank=True)
    consent_account = models.BooleanField(blank=True)
    identificador = models.StringField(label='Su código está compuesto por las iniciales de su primer nombre y apellido seguido de su fecha de nacimiento. Por ejemplo, si usted se llama Lina Ríos y usted nació el 11 de febrero de 1995, su código será LR11021995. Para iniciar por favor ingrese su código, escriba todo en mayúscula. Este código es importante para asegurar su participación en el resto de la actividad y la realización de los pagos.')
    job1_1 = models.StringField()
    job1_2 = models.StringField()
    job1_3 = models.StringField()
    job1_4 = models.StringField()
    job1_5 = models.StringField()

    #job_time_init =   models.FloatField()  # time it took the player to write his occupational aspirations
    #job_time_end =    models.FloatField()  # time it took the player to write his occupational aspirations
    # if you didn't write any option the time is 0

    def set_id(self):
            self.participant.vars['identificador'] = self.in_round(1).identificador