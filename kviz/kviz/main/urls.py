from django.urls import path
from . import views
from main.views import *

app_name = 'main' 

urlpatterns = [
    path('', views.index, name='index'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name= "logout"),
    path('kviz/', KvizList.as_view(),name='kviz'),
    path('osoba/', OsobaList.as_view(),name='osoba'),
    path('odgovori/', OdgovoriList.as_view(),name='odgovori'),
    path('pitanja/', PitanjaList.as_view(), name='pitanja'),
    path('kandidat/', KandidatListView.as_view(), name='kandidat'),
    path('unos/', views.unos_request, name='unos'),
    path('unoskandidat/', views.unoskandidat_request, name='unoskandidat'),
]