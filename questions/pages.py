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
    form_model = 'player'
    form_fields = ['mi_mundo1']
    
class mi_mundo2(Page):
    form_model = 'player'
    form_fields = ['mi_mundo2']

class mi_mundo3(Page):
    form_model = 'player'
    form_fields = ['mi_mundo3']

class mi_mundo4(Page):
    form_model = 'player'
    form_fields = ['mi_mundo4']

class mundo_trabajo(Page):
    pass

class mundo_trabajo1(Page):
    form_model = 'player'
    form_fields = ['mundo_trabajo1']

class mundo_trabajo2(Page):
    form_model = 'player'
    form_fields = ['mundo_trabajo2']

class mundo_trabajo3(Page):
    form_model = 'player'
    form_fields = ['mundo_trabajo3']

class mundo_trabajo4(Page):
    form_model = 'player'
    form_fields = ['mundo_trabajo4']

class mundo_trabajo5(Page):
    form_model = 'player'
    form_fields = ['mundo_trabajo5']

class mundo_trabajo6(Page):
    form_model = 'player'
    form_fields = ['mundo_trabajo6']

class mundo_trabajo7(Page):
    form_model = 'player'
    form_fields = ['mundo_trabajo7']

class mundo_trabajo8(Page):
    form_model = 'player'
    form_fields = ['mundo_trabajo8']

class mundo_trabajo9(Page):
    form_model = 'player'
    form_fields = ['mundo_trabajo9']

class mundo_trabajo10(Page):
    form_model = 'player'
    form_fields = ['mundo_trabajo10']

class mundo_trabajo11(Page):
    form_model = 'player'
    form_fields = ['mundo_trabajo11']

class mundo_trabajo12(Page):
    form_model = 'player'
    form_fields = ['mundo_trabajo12']

class mundo_trabajo13(Page):
    form_model = 'player'
    form_fields = ['mundo_trabajo13']

class mundo_trabajo14(Page):
    form_model = 'player'
    form_fields = ['mundo_trabajo14']

class mundo_formacion(Page):
    pass

class mundo_formacion1(Page):
    form_model = 'player'
    form_fields = ['mundo_formacion1']

class mundo_formacion2(Page):
    form_model = 'player'
    form_fields = ['mundo_formacion2']

class mundo_formacion3(Page):
    form_model = 'player'
    form_fields = ['mundo_formacion3']

class mundo_formacion4(Page):
    form_model = 'player'
    form_fields = ['mundo_formacion4']

class mundo_formacion5(Page):
    form_model = 'player'
    form_fields = ['mundo_formacion5']

class mundo_formacion6(Page):
    form_model = 'player'
    form_fields = ['mundo_formacion6']

class mundo_formacion7(Page):
    form_model = 'player'
    form_fields = ['mundo_formacion7']

class tables(Page):
    form_model = 'player'
    form_fields = ['prueba_20000', 'prueba_15000', 'prueba_10000', 'prueba_5000', 'puntaje_20000', 'puntaje_15000', 'puntaje_10000', 'puntaje_5000', 'prefer_20000', 'prefer_15000', 'prefer_10000', 'prefer_5000', 'puntaje_global']

class thanks(Page):
    pass


""""
page_sequence = [consent, ingresar, sigue , mi_mundo , mi_mundo1 , mi_mundo2 , mi_mundo3 , mi_mundo4 ,
                mundo_trabajo , mundo_trabajo1 , mundo_trabajo2 , mundo_trabajo3 , mundo_trabajo4 , 
                mundo_trabajo5 , mundo_trabajo6 , mundo_trabajo7 , mundo_trabajo8 , mundo_trabajo9 , 
                mundo_trabajo10 , mundo_trabajo11 , mundo_trabajo12 , mundo_trabajo13 ,
                mundo_formacion , mundo_formacion1 , mundo_formacion2 , mundo_formacion3 , mundo_formacion4 ,
                mundo_formacion5 , mundo_formacion6 , mundo_formacion7, thanks]

"""

page_sequence = [consent, tables]

"""
page_sequence = [consent, ingresar, sigue , mi_mundo , mi_mundo1 , mi_mundo2 , mi_mundo3 , mi_mundo4 , 
                 mundo_trabajo , mundo_trabajo1 , mundo_trabajo2 , mundo_trabajo3 , mundo_trabajo4 ,
                 mundo_trabajo5 , mundo_trabajo6 , mundo_trabajo7 , mundo_trabajo8 , mundo_trabajo9 , 
                 mundo_trabajo10 , mundo_trabajo11 , mundo_trabajo12 , mundo_trabajo13 , mundo_trabajo14 , 
                 mundo_formacion , mundo_formacion1 , mundo_formacion2 , mundo_formacion3 , mundo_formacion4 ,
                 mundo_formacion5 , mundo_formacion6 , mundo_formacion7 , tables , thanks]
"""

#page_sequence = [mundo_trabajo14]
