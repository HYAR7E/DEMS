from django.db import models
from django.contrib.auth.models import User


class ExtenUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	dni = models.CharField(max_length=8)
	name = models.CharField(max_length=55)
	ape_p = models.CharField(max_length=55)
	ape_m = models.CharField(max_length=55)
	ACCOUNT_TYPE_CHOICES = [
		("1", "Alumno"),
		("2", "Docente"),
		("3", "Admin")]
	account_type = models.CharField(choices=ACCOUNT_TYPE_CHOICES, max_length=1)

	@property
	def fullname(self):
		return (self.name+" "+self.ape_p+" "+self.ape_m).title()
	


class School(models.Model):
	name = models.CharField(max_length=55)
	ugel_num = models.CharField(max_length=12)
	direccion = models.CharField(max_length=55)

	def director(self):
		try: sxd = SchoolXDirector.objects.get(school=self)
		except SchoolXDirector.DoesNotExist: return None
		else: return sxd.director


class Director(models.Model):
	# Basic info from user
	user = models.OneToOneField(User, on_delete=models.CASCADE)


class SchoolXDirector(models.Model):
	director = models.ForeignKey(Director, on_delete=models.CASCADE)
	school = models.ForeignKey(School, on_delete=models.CASCADE)
	active = models.BooleanField(default=False)
	dt_from = models.DateField(null=True)
	dt_to = models.DateField(null=True)


class SchoolXUser(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	school = models.ForeignKey(School, on_delete=models.CASCADE)
