from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth import logout

from .forms import LoginForm


def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid():
			return HttpResponseRedirect('/')

	else:
		form = LoginForm()

		context = {
			'form': form
		}

	return render(request, 'authentication/login.html', context)


def logout(request):
	logout(request)

	return HttpResponseRedirect('/')


def adduser(request):
	pass
