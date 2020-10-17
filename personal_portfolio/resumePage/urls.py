from django.urls import path
from . import views

app_name = 'resumePage'

urlpatterns = [
    path('', views.resume, name='resume'),

]