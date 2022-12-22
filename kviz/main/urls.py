from django.urls import path
from . import views
from main.views import *

app_name = 'main' 

urlpatterns = [
    path('', views.index, name='index'),
    path("register", views.register, name="register"),
    path('kviz/', KvizList.as_view()),
    path('osoba/', OsobaList.as_view()),
    path('odgovori/', OdgovoriList.as_view()),
    path('pitanja/', PitanjaList.as_view()),
]