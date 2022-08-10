from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class consent(Page):
    form_model = 'player'
    form_fields = ['consent','consent_account']

    def is_displayed(self):
        return self.round_number == 1

class welcome(Page):
    form_model = 'player'
    form_fields = ['identificador']

    def is_displayed(self):
        return self.round_number == 1
    
    def before_next_page(self):
        self.subsession.set_id_players()

class occupation(Page):
    form_model = 'player'
  #  form_fields = ['job1_1', 'job1_2', 'job1_3', 'job1_4', 'job1_5']

    def is_displayed(self):
        return self.round_number == 1


page_sequence = [consent, welcome]
