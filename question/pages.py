from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class preguntas(Page):
    form_model = 'player'
    form_fields = ['area_1', 'time_area_1', 'area_2', 'time_area_2', 'area_3', 'time_area_3', 'area_4', 'time_area_4', 'area_5', 'time_area_5', 'time_init_area']
    def is_displayed(self):
        return self.subsession.round_number == 1

class occupation2(Page):
    form_model = 'player'
    form_fields = ['occupation_1', 'time_occupation_1', 'occupation_2', 'time_occupation_2', 'occupation_3', 'time_occupation_3', 'time_init_occupation']
    def is_displayed(self):
        return self.subsession.round_number == 1

    
  #  form_fields = ['test_job1', 'test_job2', 'test_job3', 'test_job4', 'test_job5', 'job2_1', 'job2_2', 'job2_3', 'job2_4', 'job2_5']

    def is_displayed(self):
        return self.round_number == 1

page_sequence = [preguntas, occupation2]
