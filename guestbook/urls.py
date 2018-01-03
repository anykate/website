from django.urls import path
from . import views

app_name='guestbook'

urlpatterns=[
	path('', views.index, name='index'),
	path('addcomments/', views.addcomments, name='addcommentsurl'),
]
