""" DDBB SEEDER """
from intranet.models import *
from base.models import *
from siteadmin.models import *

# User
from django.contrib.auth.models import User
kailen = User.objects.first()
s1 = User.objects.create_user(username='neldo', password='neldo123')
s2 = User.objects.create_user(username='bryan', password='bryan123')
s3 = User.objects.create_user(username='kevin', password='kevin123')
s4 = User.objects.create_user(username='sergio', password='sergio123')
s5 = User.objects.create_user(username='bruce', password='bruce123')
s6 = User.objects.create_user(username='edward', password='edward123')
s7 = User.objects.create_user(username='jimmy', password='jimmy123')
s8 = User.objects.create_user(username='barbara', password='barbara123')
s9 = User.objects.create_user(username='alice', password='alice123')
s10 = User.objects.create_user(username='sara', password='sara123')
t1 = User.objects.create_user(username='luis', password='luis123')
t2 = User.objects.create_user(username='jeff', password='jeff123')
t3 = User.objects.create_user(username='max', password='max123')
t4 = User.objects.create_user(username='karen', password='karen123')
t5 = User.objects.create_user(username='priscila', password='priscila123')

# ExtenUser
s1eu = ExtenUser.objects.create(user=s1, dni="72112258", account_type="1", name="Neldo Marrufo", ape_p="Agustin", ape_m="Falcon")
s2eu = ExtenUser.objects.create(user=s2, dni="72766277", account_type="1", name="Bryan", ape_p="Silvestre", ape_m="Monago")
s3eu = ExtenUser.objects.create(user=s3, dni="75532235", account_type="1", name="Kevin", ape_p="Godoy", ape_m="Goicochea")
s4eu = ExtenUser.objects.create(user=s4, dni="73352169", account_type="1", name="Sergio Luis", ape_p="Bonilla", ape_m="Valverde")
s5eu = ExtenUser.objects.create(user=s5, dni="00000000", account_type="1", name="Bruce", ape_p="Wayne", ape_m="Quispe")
s6eu = ExtenUser.objects.create(user=s6, dni="00000000", account_type="1", name="Edward", ape_p="Valle", ape_m="Villanueva")
s7eu = ExtenUser.objects.create(user=s7, dni="00000000", account_type="1", name="Jimmy", ape_p="Perez", ape_m="Falcon")
s8eu = ExtenUser.objects.create(user=s8, dni="00000000", account_type="1", name="Barbara", ape_p="Gonzales", ape_m="Santos")
s9eu = ExtenUser.objects.create(user=s9, dni="00000000", account_type="1", name="Alice", ape_p="Borja", ape_m="Fernandez")
s10eu = ExtenUser.objects.create(user=s10, dni="00000000", account_type="1", name="Sara", ape_p="Santacruz", ape_m="Quino")
t1eu = ExtenUser.objects.create(user=t1, dni="00000000", account_type="2", name="Luis", ape_p="Condezo", ape_m="Pajuelo")
t2eu = ExtenUser.objects.create(user=t2, dni="00000000", account_type="2", name="Jeff", ape_p="Tiburcio", ape_m="Salcedo")
t3eu = ExtenUser.objects.create(user=t3, dni="00000000", account_type="2", name="Max", ape_p="Reyes", ape_m="Bravo")
t4eu = ExtenUser.objects.create(user=t4, dni="00000000", account_type="2", name="Karen", ape_p="Albornoz", ape_m="Garcia")
t5eu = ExtenUser.objects.create(user=t5, dni="00000000", account_type="2", name="Priscila", ape_p="Esquivel", ape_m="Espinoza")
adeu = ExtenUser.objects.create(user=kailen, dni="00000000", account_type="3", name="hyarte", ape_p="zotar", ape_m="farm")

# School
school1 = School.objects.create(name="", ugel_num="32579", direccion="")

# Director
director1 = Director.objects.create(user=t3)

# Grade
gr1 = Grade.objects.create(name="1")
gr2 = Grade.objects.create(name="2")
gr3 = Grade.objects.create(name="3")
gr4 = Grade.objects.create(name="4")
gr5 = Grade.objects.create(name="5")
gr6 = Grade.objects.create(name="6")

# Section
section1 = Section.objects.create(name="A")

# SchoolXDirector
SchoolXDirector.objects.create(director=director1, school=school1, dt_from="2019-01-01")

# Student
st1 = Student.objects.create(user=s1, code="00"+s1eu.dni[::-1])
st2 = Student.objects.create(user=s2, code="00"+s2eu.dni[::-1])
st3 = Student.objects.create(user=s3, code="00"+s3eu.dni[::-1])
st4 = Student.objects.create(user=s4, code="00"+s4eu.dni[::-1])
st5 = Student.objects.create(user=s5, code="00"+s5eu.dni[::-1])
st6 = Student.objects.create(user=s6, code="00"+s6eu.dni[::-1])
st7 = Student.objects.create(user=s7, code="00"+s7eu.dni[::-1])
st8 = Student.objects.create(user=s8, code="00"+s8eu.dni[::-1])
st9 = Student.objects.create(user=s9, code="00"+s9eu.dni[::-1])
st10 = Student.objects.create(user=s10, code="00"+s10eu.dni[::-1])

# Teacher
te1 = Teacher.objects.create(user=t1, code="11"+t1eu.dni[::-1])
te2 = Teacher.objects.create(user=t2, code="11"+t2eu.dni[::-1])
te3 = Teacher.objects.create(user=t3, code="11"+t3eu.dni[::-1])
te4 = Teacher.objects.create(user=t4, code="11"+t4eu.dni[::-1])
te5 = Teacher.objects.create(user=t5, code="11"+t5eu.dni[::-1])

# StudentXGradeXSection
StudentXGradeXSection.objects.create(student=st1, grade=gr6, section=section1)
StudentXGradeXSection.objects.create(student=st2, grade=gr6, section=section1)
StudentXGradeXSection.objects.create(student=st3, grade=gr6, section=section1)
StudentXGradeXSection.objects.create(student=st4, grade=gr6, section=section1)
StudentXGradeXSection.objects.create(student=st5, grade=gr6, section=section1)
StudentXGradeXSection.objects.create(student=st6, grade=gr6, section=section1)
StudentXGradeXSection.objects.create(student=st7, grade=gr6, section=section1)
StudentXGradeXSection.objects.create(student=st8, grade=gr6, section=section1)
StudentXGradeXSection.objects.create(student=st9, grade=gr6, section=section1)
StudentXGradeXSection.objects.create(student=st10, grade=gr6, section=section1)

# TeacherXGradeXSection
TeacherXGradeXSection.objects.create(teacher=te1, grade=gr1, section=section1)
TeacherXGradeXSection.objects.create(teacher=te2, grade=gr2, section=section1)
TeacherXGradeXSection.objects.create(teacher=te3, grade=gr3, section=section1)
TeacherXGradeXSection.objects.create(teacher=te4, grade=gr4, section=section1)
TeacherXGradeXSection.objects.create(teacher=te5, grade=gr5, section=section1)
TeacherXGradeXSection.objects.create(teacher=te3, grade=gr6, section=section1)

# SchoolXUser
SchoolXUser.objects.create(school=school1, user=s1)
SchoolXUser.objects.create(school=school1, user=s2)
SchoolXUser.objects.create(school=school1, user=s3)
SchoolXUser.objects.create(school=school1, user=s4)
SchoolXUser.objects.create(school=school1, user=s5)
SchoolXUser.objects.create(school=school1, user=s6)
SchoolXUser.objects.create(school=school1, user=s7)
SchoolXUser.objects.create(school=school1, user=s8)
SchoolXUser.objects.create(school=school1, user=s9)
SchoolXUser.objects.create(school=school1, user=s10)
SchoolXUser.objects.create(school=school1, user=t1)
SchoolXUser.objects.create(school=school1, user=t2)
SchoolXUser.objects.create(school=school1, user=t3)
SchoolXUser.objects.create(school=school1, user=t4)
SchoolXUser.objects.create(school=school1, user=t5)
SchoolXUser.objects.create(school=school1, user=kailen)

# Course
Course.objects.create(name="Comunicacion Integral", total_hours="6")
Course.objects.create(name="Matematica", total_hours="8")
Course.objects.create(name="Personal Social", total_hours="4")
Course.objects.create(name="Ciencia y Ambiente", total_hours="4")
Course.objects.create(name="Educacion Fisica", total_hours="4")
Course.objects.create(name="Arte", total_hours="4")

# Syllabus
#Syllabus.objects.create()

# SyllabusTopic
#SyllabusTopic.objects.create()

# SchoolYear
SchoolYear.objects.create(dt_year="2019-01-01")
SchoolYear.objects.create(dt_year="2020-01-01")
sy = SchoolYear.objects.create(dt_year="2021-01-01")

# SchoolTrimester
stri1 = SchoolTrimester.objects.create(sc_year=sy, order=1, dt_from="2021-04-01", dt_to="2021-05-31")
stri2 = SchoolTrimester.objects.create(sc_year=sy, order=2, dt_from="2021-05-31", dt_to="2021-09-03")
stri3 = SchoolTrimester.objects.create(sc_year=sy, order=3, dt_from="2021-09-06", dt_to="2021-12-17")

# SchoolClass
#sc1 = SchoolClass.objects.create(sc_trimester=stri1, course=X,  classnumber="1")

# SchoolClassSchedule
sy = SchoolYear.objects.last()
grade1 = Grade.objects.get(name="6")
section1 = Section.objects.get(name="A")
c = Course.objects.get(pk=1) # Comunicacion
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=1, time_from="08:20", time_to="09:00", duration="00:40")
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=1, time_from="09:00", time_to="09:40", duration="00:40")
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=4, time_from="09:40", time_to="10:20", duration="00:40")
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=4, time_from="10:20", time_to="11:00", duration="00:40")
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=5, time_from="11:00", time_to="11:40", duration="00:40")
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=5, time_from="11:40", time_to="12:20", duration="00:40")
c = Course.objects.get(pk=2) # Matematicas
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=1, time_from="09:40", time_to="10:20", duration="00:40")
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=1, time_from="10:20", time_to="11:00", duration="00:40")
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=2, time_from="09:40", time_to="10:20", duration="00:40")
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=2, time_from="10:20", time_to="11:00", duration="00:40")
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=5, time_from="09:40", time_to="10:20", duration="00:40")
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=5, time_from="10:20", time_to="11:00", duration="00:40")
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=4, time_from="08:20", time_to="09:00", duration="00:40")
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=4, time_from="09:00", time_to="09:40", duration="00:40")
c = Course.objects.get(pk=3) # Personal Social
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=2, time_from="11:00", time_to="11:40", duration="00:40")
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=2, time_from="11:40", time_to="12:20", duration="00:40")
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=3, time_from="11:00", time_to="11:40", duration="00:40")
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=3, time_from="11:40", time_to="12:20", duration="00:40")
c = Course.objects.get(pk=4) # Ciencia y Ambiente
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=3, time_from="09:40", time_to="10:20", duration="00:40")
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=3, time_from="10:20", time_to="11:00", duration="00:40")
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=4, time_from="11:00", time_to="11:40", duration="00:40")
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=4, time_from="11:40", time_to="12:20", duration="00:40")
c = Course.objects.get(pk=5) # Educacion Fisica
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=1, time_from="11:00", time_to="11:40", duration="00:40")
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=1, time_from="11:40", time_to="12:20", duration="00:40")
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=5, time_from="08:20", time_to="09:00", duration="00:40")
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=5, time_from="09:00", time_to="09:40", duration="00:40")
c = Course.objects.get(pk=6) # Arte
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=2, time_from="08:20", time_to="09:00", duration="00:40")
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=2, time_from="09:00", time_to="09:40", duration="00:40")
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=3, time_from="08:20", time_to="09:00", duration="00:40")
SchoolClassSchedule.objects.create(course=c, sc_year=sy, grade=grade1, section=section1, dt_day=3, time_from="09:00", time_to="09:40", duration="00:40")


"""
08:20 - 12:20
 1da  -  6ma

4 horas -> 6 sesiones
1 sesion -> 40 mins
"""


# CompetenciaXCurso
c = Course.objects.get(pk=1) # Comunicacion
CompetenciaXCurso.objects.create(course=c, competencia="Argumenta con claridad utilizando expresiones formales y coloquiales, cuando participa en conversatorios y debates sobre temas relacionados con el uso racional, la importancia y la contaminaci??n del agua")
CompetenciaXCurso.objects.create(course=c, competencia="El debate. El discurso")
CompetenciaXCurso.objects.create(course=c, competencia="Demuestra seguridad y confianza al manifestar su punto de vista con respecto al uso adecuado del agua y sensibilidad frente a su contaminaci??n")
c = Course.objects.get(pk=2) # Matematicas
CompetenciaXCurso.objects.create(course=c, competencia="Resuelve y formula problemas que implican operaciones combinadas con n??meros naturales, fracciones y decimales")
CompetenciaXCurso.objects.create(course=c, competencia="Operaciones combinadas con n??meros naturales, fracciones y decimales")
CompetenciaXCurso.objects.create(course=c, competencia="Mide y compara el volumen de s??lidos en unidades arbitrarias de medida")
c = Course.objects.get(pk=3) # Personal Social
CompetenciaXCurso.objects.create(course=c, competencia="Investiga e identifica las instituciones de gobierno local, regional nacional y explica las funciones que cumplen en el desarrollo y conservaci??n del y su repercusi??n mundial")
CompetenciaXCurso.objects.create(course=c, competencia="Estado peruano: Poderes del Estado. ??rganos Constitucionales Aut??nomos")
CompetenciaXCurso.objects.create(course=c, competencia="Manifiesta placer o malestar ante determinadas situaciones que lo afectan positiva o negativamente en su interacci??n con los dem??s y el medio que lo rodea")
c = Course.objects.get(pk=4) # Ciencia y Ambiente
CompetenciaXCurso.objects.create(course=c, competencia="Energ??a el??ctrica. Artefactos el??ctricos. Consumo de energ??a en kilowatthora. Equivalencia en focos incandescentes. Costos del consumo. Estrategias de ahorro de energ??a")
CompetenciaXCurso.objects.create(course=c, competencia="Contaminaci??n ambiental: emisiones de carbono y sus efectos en el ambiente")
CompetenciaXCurso.objects.create(course=c, competencia="Destrucci??n de la capa de ozono; medidas para contrarrestar sus impactos")
c = Course.objects.get(pk=5) # Educacion Fisica
CompetenciaXCurso.objects.create(course=c, competencia="Utiliza y combina creativamente sus habilidades b??sicas en actividades variadas")
CompetenciaXCurso.objects.create(course=c, competencia="Nociones de las habilidades combinadas")
CompetenciaXCurso.objects.create(course=c, competencia="Demuestra agrado y disposici??n para la realizaci??n de actividades motrices que contribuyen a la conservaci??n del ambiente para la realizaci??n de actividades motrices")
c = Course.objects.get(pk=6) # Arte
CompetenciaXCurso.objects.create(course=c, competencia="Taller #1")
CompetenciaXCurso.objects.create(course=c, competencia="Taller #2")
CompetenciaXCurso.objects.create(course=c, competencia="Taller #3")

# NotaXTrimester
from intranet.models import *
from base.models import *
from siteadmin.models import *
import random
for s in Student.objects.all():
    for cxc in CompetenciaXCurso.objects.all():
        for tri in SchoolTrimester.objects.all():
            NotaXTrimester.objects.create(student=s, competencia=cxc, sc_trimester=tri, nota=random.randrange(5, 20))

# Attendance
from intranet.models import *
from base.models import *
from siteadmin.models import *
import random
import datetime as dt
for s in Student.objects.all():
    for tri in SchoolTrimester.objects.all():
        # Iterate over date
        d = dt.timedelta(days=1)
        _date = tri.dt_from
        while _date <= tri.dt_to:
            if _date.isoweekday() <= 5:
                Attendance.objects.create(student=s, sc_trimester=tri, dt=_date, status=(random.randrange(1, 10)>3))
            _date = _date +d

# SchoolClass
grade1 = Grade.objects.get(name="6")
for c in Course.objects.all():
    i = 0
    for tri in SchoolTrimester.objects.all():
        _scs = SchoolClassSchedule.objects.filter(grade=grade1, course=c).values('dt_day').distinct()
        _days = [int(_s.get('dt_day')) for _s in _scs]
        _dt = tri.dt_from
        d = dt.timedelta(days=1)
        while _dt <= tri.dt_to:
            if _dt.isoweekday() in _days:
                i+=1
                SchoolClass.objects.create(sc_trimester=tri, grade=grade1, course=c, dt=_dt, classnumber=i)
            _dt = _dt + d
