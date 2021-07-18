from django.db import models
from django.contrib.auth.models import User
from siteadmin.models import School, ExtenUser


class Student(models.Model):
	# Basic info from user
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	code = models.CharField(max_length=55)

	@property
	def meta(self):
		return ExtenUser.objects.get(user=self.user)

	""" Student(1, User(1)) """


class Teacher(models.Model):
	# Basic info from user
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	code = models.CharField(max_length=55)

	@property
	def meta(self):
		return ExtenUser.objects.get(user=self.user)

	""" Teacher(1, User(2)) """


class Grade(models.Model):
	name = models.CharField(max_length=55)

	""" Grade(1, "1"), Grade(2, "2"), Grade(3, "3") """


class Section(models.Model):
	name = models.CharField(max_length=2)

	""" Section(1, "A"), Section(2, "B"), Section(3, "C") """


class TeacherXGradeXSection(models.Model):
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
	section = models.ForeignKey(Section, on_delete=models.CASCADE)

	""" TXGXS(1, Teacher(1), Grade(1), Section(1)) """


class StudentXGradeXSection(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
	section = models.ForeignKey(Section, on_delete=models.CASCADE)

	""" AXGXS(1, Alumno(1), Grade(1), Section(1)) """


class Course(models.Model):
	name = models.CharField(max_length=55)
	total_hours = models.CharField(max_length=2)


class GDriveFile(models.Model):
	file_id = models.CharField(max_length=255)
	filename = models.CharField(max_length=255)
	description = models.TextField()
	webViewLink = models.CharField(max_length=255)
	webContentLink = models.CharField(max_length=255)
	upload_date = models.DateTimeField()
	created = models.DateTimeField(auto_now_add=True)


""" AVANCE CURRICULAR """


class Syllabus(models.Model):
	""" document """
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
	document = models.ForeignKey(GDriveFile, on_delete=models.CASCADE)


class SyllabusTopic(models.Model):
	""" topic by class """
	syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	classnumber = models.CharField(max_length=2)


class SchoolYear(models.Model):
	dt_year = models.DateField()
	dt_from = models.DateField(null=True)
	dt_to = models.DateField(null=True)


class SchoolTrimester(models.Model):
	sc_year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)
	dt_from = models.DateField(null=True)
	dt_to = models.DateField(null=True)
	ORDER_CHOICES = [
		("1", "1er Trimestre"),
		("2", "2do Trimestre"),
		("3", "3er Trimestre")]
	order = models.CharField(choices=ORDER_CHOICES, max_length=1)


class SchoolClass(models.Model):
	sc_trimester = models.ForeignKey(SchoolTrimester, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
	dt = models.DateField(null=True)
	classnumber = models.CharField(max_length=3)
	gdrive_folder_id = models.CharField(max_length=255, null=True, default=None)


class SchoolClassSchedule(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	sc_year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)
	grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
	section = models.ForeignKey(Section, on_delete=models.CASCADE)
	duration = models.TimeField()
	time_from = models.TimeField()
	time_to = models.TimeField()
	DAY_CHOICES = [
		("1", "Lunes"),
		("2", "Martes"),
		("3", "Miercoles"),
		("4", "Jueves"),
		("5", "Viernes")]
	dt_day = models.CharField(choices=DAY_CHOICES, max_length=1)


""" NOTAS """


class CompetenciaXCurso(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	competencia = models.CharField(max_length=255)

	""" CXC(1, 1, "comp1"), CXC(2, 1, "comp2") """


class NotaXTrimester(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	competencia = models.ForeignKey(CompetenciaXCurso, on_delete=models.CASCADE)
	sc_trimester = models.ForeignKey(SchoolTrimester, on_delete=models.CASCADE)
	nota = models.IntegerField()

	""" NXT(1, 1, 1, 16), NXT(2, 1, 1, 14), NXT(3, 1, 1, 18) """


""" AVANCE CURRICULAR """



class Attendance(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	sc_trimester = models.ForeignKey(SchoolTrimester, on_delete=models.CASCADE)
	dt = models.DateField()
	status = models.BooleanField(default=False)
