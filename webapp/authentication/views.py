from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import LoginForm, AddUserForm
from .models import User


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
			username=form.cleaned_data['username'],
			password=form.cleaned_data['password'],
			email=form.cleaned_data['email']
		)
		return HttpResponseRedirect('/')

	variables = {
		'form': form
	}
	return render(request, 'authentication/add_user.html', variables)


def verify(request, uuid):
	try:
		user = User.objects.get(verification_uuid=uuid, is_verified=False)
	except User.DoesNotExist:
		raise Http404("User does not exist or is already verified")

	user.is_verified = True
	user.save()

	return redirect('/authentication/login')
