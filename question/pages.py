from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class preguntas(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1

class occupation2(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1

    form_model = 'player'
  #  form_fields = ['test_job1', 'test_job2', 'test_job3', 'test_job4', 'test_job5', 'job2_1', 'job2_2', 'job2_3', 'job2_4', 'job2_5']

    def is_displayed(self):
        return self.round_number == 1

page_sequence = [preguntas, occupation2]
