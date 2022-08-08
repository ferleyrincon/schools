from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class occupation2(Page):
    form_model = 'player'
  #  form_fields = ['test_job1', 'test_job2', 'test_job3', 'test_job4', 'test_job5', 'job2_1', 'job2_2', 'job2_3', 'job2_4', 'job2_5']

    def is_displayed(self):
        return self.round_number == 1


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [occupation2, ResultsWaitPage, Results]
