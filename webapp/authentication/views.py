from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import LoginForm, AddUserForm


def log_in(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = authenticate(request, username=username, password=password)

			if user:
				login(request, user)
				return HttpResponseRedirect('/')

			else:
				form = LoginForm(error_class='1488')

				context = {
					'form': form
				}

				return render(request, 'authentication/login.html', context)

	form = LoginForm()

	context = {
		'form': form
	}

	return render(request, 'authentication/login.html', context)


def log_out(request):
	logout(request)

	return HttpResponseRedirect('/')


def add_user(request):
	form = AddUserForm(request.POST or None)
	if form.is_valid():
		User.objects.create_user(
			username=form.clean_data['username'],
			password=form.clean_data['password1'],
			email=form.clean_data['email']
		)
		return HttpResponseRedirect('/')

	variables = {
		'form': form
	}
	return render(request, 'authentication/add_user.html', variables)
