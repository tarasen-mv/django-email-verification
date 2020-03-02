from django.urls import path

from . import views

urlpatterns = [
	path('login', views.login, name='login'),
	path('logout', views.logout, name='logout'),
	path('adduser', views.adduser, name='adduser'),
]
