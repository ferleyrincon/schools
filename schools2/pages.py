from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class consent(Page):
    form_model = 'player'
    form_fields = ['consent','consent_account']

    def is_displayed(self):
        return self.round_number == 1

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [consent, ResultsWaitPage, Results]
