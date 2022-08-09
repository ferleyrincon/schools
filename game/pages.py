from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class quiz_answer(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):
        return {
            "camila" : self.participant.vars['camila']
        }

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
    form_model = 'player'
    form_fields = ['p2_a1', 'p2_a2']

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        situacion = random.randint(1, 6)
        pago = 0
        pago += self.player.p2_a1 + ((self.player.p2_a1*Constants.profitability[2][situacion]['i1'])/100)
        print("Asignacion 1: {:s} | Situacion # {:s} | Rentabilidad {:s}".format(str(self.player.p2_a1), str(situacion), str(Constants.profitability[2][situacion]['i1'])))
        print(" -> Pago acumulado {:s}".format(str(pago)))
        pago += self.player.p2_a2 + ((self.player.p2_a2*Constants.profitability[2][situacion]['i2'])/100)
        print("Asignacion 2: {:s} | Situacion # {:s} | Rentabilidad {:s}".format(str(self.player.p2_a2), str(situacion), str(Constants.profitability[2][situacion]['i2'])))
        print(" -> Pago acumulado {:s}".format(str(pago)))
        self.player.p2_r1 = Constants.profitability[2][situacion]['i1']
        self.player.p2_r2 = Constants.profitability[2][situacion]['i2']
        self.player.p2_p = int(pago)

    def vars_for_template(self):
        return{
            "profitability": Constants.profitability[2]
        }


class decision3(Page):
    form_model = 'player'
    form_fields = ['p3_a1', 'p3_a2']

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        situacion = random.randint(1, 6)
        pago = 0
        pago += self.player.p3_a1 + ((self.player.p3_a1*Constants.profitability[3][situacion]['i1'])/100)
        print("Asignacion 1: {:s} | Situacion # {:s} | Rentabilidad {:s}".format(str(self.player.p3_a1), str(situacion), str(Constants.profitability[3][situacion]['i1'])))
        print(" -> Pago acumulado {:s}".format(str(pago)))
        pago += self.player.p3_a2 + ((self.player.p3_a2*Constants.profitability[3][situacion]['i2'])/100)
        print("Asignacion 2: {:s} | Situacion # {:s} | Rentabilidad {:s}".format(str(self.player.p3_a2), str(situacion), str(Constants.profitability[3][situacion]['i2'])))
        print(" -> Pago acumulado {:s}".format(str(pago)))
        self.player.p3_r1 = Constants.profitability[3][situacion]['i1']
        self.player.p3_r2 = Constants.profitability[3][situacion]['i2']
        self.player.p3_p = int(pago)

    def vars_for_template(self):
        return{
            "profitability": Constants.profitability[3]
        }


class decision4(Page):
    form_model = 'player'
    form_fields = ['p4_a1', 'p4_a2']

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        situacion = random.randint(1, 6)
        pago = 0
        pago += self.player.p4_a1 + ((self.player.p4_a1*Constants.profitability[4][situacion]['i1'])/100)
        print("Asignacion 1: {:s} | Situacion # {:s} | Rentabilidad {:s}".format(str(self.player.p4_a1), str(situacion), str(Constants.profitability[4][situacion]['i1'])))
        print(" -> Pago acumulado {:s}".format(str(pago)))
        pago += self.player.p4_a2 + ((self.player.p4_a2*Constants.profitability[4][situacion]['i2'])/100)
        print("Asignacion 2: {:s} | Situacion # {:s} | Rentabilidad {:s}".format(str(self.player.p4_a2), str(situacion), str(Constants.profitability[4][situacion]['i2'])))
        print(" -> Pago acumulado {:s}".format(str(pago)))
        self.player.p4_r1 = Constants.profitability[4][situacion]['i1']
        self.player.p4_r2 = Constants.profitability[4][situacion]['i2']
        self.player.p4_p = int(pago)

    def vars_for_template(self):
        return{
            "profitability": Constants.profitability[4]
        }

class decision5(Page):
    form_model = 'player'
    form_fields = ['p5_a1', 'p5_a2']

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        situacion = random.randint(1, 6)
        pago = 0
        pago += self.player.p5_a1 + ((self.player.p5_a1*Constants.profitability[5][situacion]['i1'])/100)
        print("Asignacion 1: {:s} | Situacion # {:s} | Rentabilidad {:s}".format(str(self.player.p5_a1), str(situacion), str(Constants.profitability[5][situacion]['i1'])))
        print(" -> Pago acumulado {:s}".format(str(pago)))
        pago += self.player.p5_a2 + ((self.player.p5_a2*Constants.profitability[5][situacion]['i2'])/100)
        print("Asignacion 2: {:s} | Situacion # {:s} | Rentabilidad {:s}".format(str(self.player.p5_a2), str(situacion), str(Constants.profitability[5][situacion]['i2'])))
        print(" -> Pago acumulado {:s}".format(str(pago)))
        self.player.p5_r1 = Constants.profitability[5][situacion]['i1']
        self.player.p5_r2 = Constants.profitability[5][situacion]['i2']
        self.player.p5_p = int(pago)

    def vars_for_template(self):
        return{
            "profitability": Constants.profitability[5]
        }


class decision6(Page):
    form_model = 'player'
    form_fields = ['p6_a1', 'p6_a2']

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        situacion = random.randint(1, 6)
        pago = 0
        pago += self.player.p6_a1 + ((self.player.p6_a1*Constants.profitability[6][situacion]['i1'])/100)
        print("Asignacion 1: {:s} | Situacion # {:s} | Rentabilidad {:s}".format(str(self.player.p6_a1), str(situacion), str(Constants.profitability[6][situacion]['i1'])))
        print(" -> Pago acumulado {:s}".format(str(pago)))
        pago += self.player.p6_a2 + ((self.player.p6_a2*Constants.profitability[2][situacion]['i2'])/100)
        print("Asignacion 2: {:s} | Situacion # {:s} | Rentabilidad {:s}".format(str(self.player.p6_a2), str(situacion), str(Constants.profitability[6][situacion]['i2'])))
        print(" -> Pago acumulado {:s}".format(str(pago)))
        self.player.p6_r1 = Constants.profitability[6][situacion]['i1']
        self.player.p6_r2 = Constants.profitability[6][situacion]['i2']
        self.player.p6_p = int(pago)

    def vars_for_template(self):
        return{
            "profitability": Constants.profitability[6]
        }

class instructions_game(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return{
            "profitability": Constants.profitability[3],
            "investment1" : self.participant.vars['investment1']
        }

class wait(WaitPage):
    def after_all_players_arrive(self):
        totalPago = random.choice([self.group.get_players()[0].p1_p, self.group.get_players()[0].p2_p, self.group.get_players()[0].p3_p, self.group.get_players()[0].p4_p, self.group.get_players()[0].p5_p, self.group.get_players()[0].p6_p])
        self.group.get_players()[0].payoff = totalPago

class payoff(Page):
    def vars_for_template(self):
        return{
            'payoff': self.player.participant.payoff
        }


page_sequence = [instructions_game, decision1, decision2, decision3, decision4, decision5, decision6, wait, payoff]
