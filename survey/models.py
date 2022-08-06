from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    job2_1 = models.StringField()
    job2_2 = models.StringField()
    job2_3 = models.StringField()
    job2_4 = models.StringField()
    job2_5 = models.StringField()

    prueba_20000 = models.StringField();
    prueba_15000 = models.StringField();
    prueba_10000 = models.StringField();
    prueba_5000 = models.StringField();

    puntaje_20000 = models.IntegerField();
    puntaje_15000 = models.IntegerField();
    puntaje_10000 = models.IntegerField();
    puntaje_5000 = models.IntegerField();

    prefer_20000 = models.IntegerField();
    prefer_15000 = models.IntegerField();
    prefer_10000 = models.IntegerField();
    prefer_5000 = models.IntegerField();

    grupo_puntaje_global = models.IntegerField();

    educ_type = models.IntegerField(
    choices=[
        [1,'Técnica'],
        [2,'Tecnológica'],
        [3,'Profesional'],
        [4,'Ninguna']
    ], label="¿Para hacer lo que más le gusta es necesaria una carrera?")

    educ_university = models.StringField(label="Escriba el nombre de la institución en la que desea estudiar:")

    efficacy1 =  models.IntegerField()
    check_slider_efficacy1 =  models.IntegerField()

    efficacy2 =  models.IntegerField()
    check_slider_efficacy2 =  models.IntegerField()

    efficacy3 =  models.IntegerField()
    check_slider_efficacy3 =  models.IntegerField()

    efficacy4 =  models.IntegerField()
    check_slider_efficacy4 =  models.IntegerField()

    educsup =  models.IntegerField()
    check_slider_educsup=  models.IntegerField()


    p_sex = models.IntegerField(
    choices=[
        [1, 'Hombre'],
        [2, 'Mujer'],
        [3, 'Otro'],
    ], label="2. ¿Cuál es su sexo?")

    p_age = models.IntegerField(label="3. Edad")

    p_work = models.IntegerField(
    choices=[
        [1, 'No, solo estudio.'],
        [2, 'Sí, para ganar dinero para mis gastos.'],
        [3, 'Sí, para ayudar con los gastos familiares.'],
        [4, 'Sí, para obtener experiencia laboral.'],
        [5, 'Sí, para ganar dinero para mis gastos'],
        [6, 'Sí, para hacer contactos que podrían llevarle a encontrar un trabajo. '],
        [7, 'Sí, por otra razón '],
    ], label="4. ¿Ha trabajado y estudiado al mismo tiempo? ¿Cuál fue su motivo principal para trabajar mientras estudiaba?")

    p_hwork = models.IntegerField(label="5. ¿Cuántas horas trabajó usted durante la semana pasada?")

    p_wage = models.IntegerField(
    choices=[
        [1, 'No.'],
        [2, 'Si, en efectivo.'],
        [3, 'Si, en especie.'],
        [4, 'Si, en efectivo y especie.'],
    ], label="6. ¿Usted recibe algún tipo de remuneración por trabajar?")

    p_wage = models.IntegerField(
    choices=[
        [1, 'No.'],
        [2, 'Sí, por dificultades académicas.'],
        [3, 'Sí, por dificultades en el colegio con compañeros, docentes o directivos.'],
        [4, 'Sí, por enfermedad.'],
        [5, 'Sí, por falta de interés en estudiar.'],
        [6, 'Sí, por razones económicas.'],
        [7, 'Sí, por razones de seguridad (nivel de violencia en la zona).'],
    ], label="7. ¿Alguna vez tuvo que suspender sus estudios?")

    p_years = models.IntegerField(
    choices=[
        [1, 'No, no he perdido ningún año.'],
        [2, 'Sí, estudié y no aprobé los exámenes.'],
        [3, 'Sí, por dificultades en el colegio con compañeros, docentes o directivos.'],
        [4, 'Sí, por enfermedad.'],
        [5, 'Sí, no me interesaban los temas.'],
        [6, 'Sí, por razones económicas.'],
        [7, 'Sí, tenía poco tiempo después del colegio para estudiar.'],
    ], label="8. ¿Ha reprobado algún año?")

    p_family = models.IntegerField(min=0, max=15, label="9.	¿Cuántas personas conforman el hogar donde vive actualmente, incluido usted? ")

    p_rooms = models.IntegerField(min=0, max=10, label="10.	En total, ¿en cuántos cuartos duermen las personas de su hogar?")

    p_internet = models.IntegerField(
    choices=[
        [1, 'No.'],
        [2, 'Sí, hay un teléfono móvil con datos.'],
        [3, 'Sí, hay un computador portátil con conexión a internet.'],
        [4, 'Sí, hay un computador de escritorio con conexión a internet.'],
    ], label="11. ¿En su hogar cuenta con acceso o conexión a internet?")

    p_tinternet = models.IntegerField(
    choices=[
        [1, 'No usa internet'],
        [2, '30 minutos o menos'],
        [3, 'Entre 30 y 60 minutos'],
        [4, 'Entre 1 y 3 horas'],
        [5, 'Más de 3 horas'],
    ], label="12. Usualmente, ¿cuánto tiempo al DÍA dedica a navegar en internet?")

    p_poverty = models.IntegerField(
    choices=[
        [1, 'Muy buenas'],
        [2, 'Buenas'],
        [3, 'Regulares'],
        [4, 'Malas'],
    ], label="13. ¿Cómo describiría las condiciones económicas de su hogar?")

    p_poverty = models.IntegerField(
    choices=[
        [1, 'Muy buenas'],
        [2, 'Buenas'],
        [3, 'Regulares'],
        [4, 'Malas'],
    ], label="13. ¿Cómo describiría las condiciones económicas de su hogar?")

    p_care = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    widget=widgets.RadioSelect,
    label="14. De 1 a 5, ¿qué tanto cree que ayudar en su casa dificulta su proceso de aprendizaje?")

    p_migration = models.IntegerField(
    choices=[
        [1, 'No.'],
        [2, 'Sí, por trabajo.'],
        [3, 'Sí, por educación.'],
        [4, 'Sí, por salud.'],
        [5, 'Sí, por las condiciones de seguridad.'],
        [6, 'Sí, otra razón.'],
    ], label="15. El siguiente año, ¿cree que se va vivir a otro municipio?")

    p_health = models.IntegerField(
    choices=[
        [1,'Subsidiado'],
        [2,'Contributivo (incluye regímenes especiales)']
    ], label="16. ¿A qué régimen de seguridad social en salud pertenece?")

    p_pension2 = models.IntegerField(
    choices=[
        [1,'Aportando en un fondo de pensiones obligatorias'],
        [2,'Aportando en un fondo de pensiones voluntarias (por ejemplo, BEPS)'],
        [3,'Ahorrando'],
        [4,'Haciendo inversiones'],
        [5,'Pagando un seguro por su cuenta'],
        [6,'Preparando a los hijos para que puedan ayudarlos en su vejez'],
        [7,'Nada'],
    ], label="17. ¿Qué están haciendo (hicieron) sus padres para mantenerse económicamente en la vejez?")

    icfes_m1 = models.StringField(choices=['A', 'B', 'C', 'D'], widget=widgets.RadioSelectHorizontal, label="Seleccione solo UNA respuesta:")
    icfes_m2 = models.StringField(choices=['A', 'B', 'C', 'D'], widget=widgets.RadioSelectHorizontal, label="Seleccione solo UNA respuesta:")
    icfes_l1 = models.StringField(choices=['A', 'B', 'C', 'D'], widget=widgets.RadioSelectHorizontal, label="Seleccione solo UNA respuesta:")
    icfes_l2 = models.StringField(choices=['A', 'B', 'C', 'D'], widget=widgets.RadioSelectHorizontal, label="Seleccione solo UNA respuesta:")
    icfes_n1 = models.StringField(choices=['A', 'B', 'C', 'D'], widget=widgets.RadioSelectHorizontal, label="Seleccione solo UNA respuesta:")
    icfes_n2 = models.StringField(choices=['A', 'B', 'C', 'D'], widget=widgets.RadioSelectHorizontal, label="Seleccione solo UNA respuesta:")
    icfes_s1 = models.StringField(choices=['A', 'B', 'C', 'D'], widget=widgets.RadioSelectHorizontal, label="Seleccione solo UNA respuesta:")
    icfes_s2 = models.StringField(choices=['A', 'B', 'C', 'D'], widget=widgets.RadioSelectHorizontal, label="Seleccione solo UNA respuesta:")



    












