from django.db import models
from django.contrib.auth.models import User


class Publication(models.Model):
	name = models.CharField(max_length=255)
	content = models.TextField()
	author = models.OneToOneField(User, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now=True)
