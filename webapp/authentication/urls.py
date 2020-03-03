from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
	path('login', views.log_in, name='login'),
	path('logout', views.log_out, name='logout'),
	path('adduser', views.add_user, name='adduser'),
	url(r'verify/(?P<uuid>[a-z0-9\-]+)/', views.verify, name='verify')
]
