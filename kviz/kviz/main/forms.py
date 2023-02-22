from django import forms
from django.shortcuts import render
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import * 

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=False)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class PretragaForm(forms.ModelForm):
	class Meta:
		model = Kviz
		fields = ("imeKviza","tezina","kategorija")
		labels = {'imeKviza': "Ime kviza", "tezina": "Tezina kviza","kategorija": "Kategorija kviza"}
		
class KandidatForm(forms.ModelForm):
	class Meta:
		model = Kandidat
		fields = ("ime","prezime","godine")
		labels = {'ime': "Ime", "prezime": "Prezime","godine": "Godine"}

class KvizUnos(forms.ModelForm):
  class Meta:
    model = Kviz
    fields = ["imeKviza","tezina","kategorija"]
    labels = {'imeKviza': "Ime kviza", "tezina": "Tezina kviza","kategorija": "Kategorija kviza"}
