from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class consent(Page):
    form_model = 'player'
    form_fields = ['consent','consent_account']

    def is_displayed(self):
        return self.round_number == 1

class ingresar(Page):
    pass

class sigue(Page):
    pass

class ruta(Page):
    pass

class mi_mundo(Page):
    pass

class mi_mundo1(Page):
    pass

class mi_mundo2(Page):
    pass

class mi_mundo3(Page):
    pass

class mi_mundo4(Page):
    pass

class mundo_trabajo(Page):
    pass

class mundo_trabajo1(Page):
    pass

class mundo_trabajo2(Page):
    pass

class mundo_trabajo3(Page):
    pass

class mundo_trabajo4(Page):
    pass

class mundo_trabajo5(Page):
    pass

class mundo_trabajo6(Page):
    pass

class mundo_trabajo7(Page):
    pass

class mundo_trabajo8(Page):
    pass

class mundo_trabajo9(Page):
    pass

class mundo_trabajo10(Page):
    pass

class mundo_trabajo11(Page):
    pass

class mundo_trabajo12(Page):
    pass

class mundo_trabajo13(Page):
    pass

class mundo_trabajo14(Page):
    pass

class mundo_formacion(Page):
    pass

class mundo_formacion1(Page):
    pass

class mundo_formacion2(Page):
    pass

class mundo_formacion3(Page):
    pass

class mundo_formacion4(Page):
    pass

class mundo_formacion5(Page):
    pass

class mundo_formacion6(Page):
    pass

class mundo_formacion7(Page):
    pass

class thanks(Page):
    pass

#page_sequence = [consent, ingresar, sigue , ruta , mi_mundo , mi_mundo1 , mi_mundo2 , mi_mundo3 , mi_mundo4 ,
#                mundo_trabajo , mundo_trabajo1 , mundo_trabajo2 , mundo_trabajo3 , mundo_trabajo4 , 
#                mundo_trabajo5 , mundo_trabajo6 , mundo_trabajo7 , mundo_trabajo8 , mundo_trabajo9 , 
#                mundo_trabajo10 , mundo_trabajo11 , mundo_trabajo12 , mundo_trabajo13 , mundo_trabajo14 ,
#                mundo_formacion , mundo_formacion1 , mundo_formacion2 , mundo_formacion3 , mundo_formacion4 ,
#                mundo_formacion5, mundo_formacion5, mundo_formacion7, thanks]

page_sequence = [consent, ingresar, sigue,          mi_mundo , mi_mundo1 , mi_mundo2 , mi_mundo3 , mi_mundo4 , 
                 mundo_trabajo , mundo_trabajo1 , mundo_trabajo2 , mundo_trabajo3 , mundo_trabajo4 ,
                 mundo_trabajo5 , mundo_trabajo6 , mundo_trabajo7 ,                  mundo_trabajo9 , 
                 mundo_trabajo10]

#page_sequence = [mi_mundo3]