from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class decision1(Page):
    form_model = 'player'
    form_fields = ['p1_a1', 'p1_a2']

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        situacion = random.randint(1, 6)
        pago = 0
        pago += self.player.p1_a1 + ((self.player.p1_a1*Constants.profitability[1][situacion]['i1'])/100)
        print("Asignacion 1: {:s} | Situacion # {:s} | Rentabilidad {:s}".format(str(self.player.p1_a1), str(situacion), str(Constants.profitability[1][situacion]['i1'])))
        print(" -> Pago acumulado {:s}".format(str(pago)))
        pago += self.player.p1_a2 + ((self.player.p1_a2*Constants.profitability[1][situacion]['i2'])/100)
        print("Asignacion 2: {:s} | Situacion # {:s} | Rentabilidad {:s}".format(str(self.player.p1_a2), str(situacion), str(Constants.profitability[1][situacion]['i2'])))
        print(" -> Pago acumulado {:s}".format(str(pago)))
        self.player.p1_r1 = Constants.profitability[1][situacion]['i1']
        self.player.p1_r2 = Constants.profitability[1][situacion]['i2']
        self.player.p1_p = int(pago)

    def vars_for_template(self):
        return{
            "profitability": Constants.profitability[1]
        }


class decision2(Page):
    pass


class decision3(Page):
    pass


class decision4(Page):
    pass


class decision5(Page):
    pass


class decision6(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [decision1]
