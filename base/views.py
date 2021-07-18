from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect as HttpRD
from django.contrib.auth import authenticate, login as authlogin

from siteadmin.models import School


def index(req):
	try:
		s = School.objects.first()
	except School.DoesNotExist:
		raise Http404("El colegio no existe")
	ctx = {'school': s}
	return render(req, 'base/index.html', ctx)


def login(req):
	if req.user.is_authenticated:
		return HttpRD(reverse('intranet:index'))
	# POST data
	username = req.POST.get('username', "")
	password = req.POST.get('password', "")
	# No data sent
	if username=="" or password=="":
		return render(req, 'base/login.html')
	# Try to log in
	user = authenticate(req, username=username, password=password)

	if not user: return render(req, 'base/login.html', {'er': "Usuario o contraseña incorrecto"})
	else:
		authlogin(req, user)
		return HttpRD(reverse('intranet:index'))
