from django.contrib import admin
from .models import *

model_list = [Kviz, Osoba, Pitanja, Odgovori]
admin.site.register(model_list)