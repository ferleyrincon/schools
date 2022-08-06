from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class occupation2(Page):
    form_model = 'player'
  #  form_fields = ['job1_1', 'job1_2', 'job1_3', 'job1_4', 'job1_5']
    form_fields = ['educ_type', "educ_university"]

    def is_displayed(self):
        return self.round_number == 1

class saber11(Page):
    form_model = 'player'
    form_fields = ['prueba_20000', 'prueba_15000', 'prueba_10000', 'prueba_5000', 'puntaje_20000', 'puntaje_15000', 'puntaje_10000', 'puntaje_5000', 'prefer_20000', 'prefer_15000', 'prefer_10000', 'prefer_5000', 'puntaje_global']

def is_displayed(self):
        return self.round_number == 1

class selfefficacy(Page):
    form_model = 'player'
    form_fields = ['efficacy1','check_slider_efficacy1','efficacy2','check_slider_efficacy2','efficacy3','check_slider_efficacy3','efficacy4','check_slider_efficacy4']

def is_displayed(self):
        return self.round_number == 1

class education(Page):
    form_model = 'player'
    form_fields = ['educsup', 'check_slider_educsup']

    def is_displayed(self):
        return self.round_number == 1

class icfes_m1(Page):
    form_model = 'player'
    form_fields = ['icfes_m1']

    def is_displayed(self):
        return self.round_number == 1

class icfes_m2(Page):
    form_model = 'player'
    form_fields = ['icfes_m2']

    def is_displayed(self):
        return self.round_number == 1

class icfes_l1(Page):
    form_model = 'player'
    form_fields = ['icfes_l1']

    def is_displayed(self):
        return self.round_number == 1

class icfes_l2(Page):
    form_model = 'player'
    form_fields = ['icfes_l2']

    def is_displayed(self):
        return self.round_number == 1

class icfes_n1(Page):
    form_model = 'player'
    form_fields = ['icfes_n1']

    def is_displayed(self):
        return self.round_number == 1

class icfes_n2(Page):
    form_model = 'player'
    form_fields = ['icfes_n2']

    def is_displayed(self):
        return self.round_number == 1

class icfes_s1(Page):
    form_model = 'player'
    form_fields = ['icfes_s1']

    def is_displayed(self):
        return self.round_number == 1

class icfes_s2(Page):
    form_model = 'player'
    form_fields = ['icfes_s2']

    def is_displayed(self):
        return self.round_number == 1


page_sequence = [icfes_m1, icfes_m2, icfes_l1, icfes_l2, icfes_n1, icfes_n2, icfes_s1, icfes_s2, education, occupation2, saber11, selfefficacy]
