from django.shortcuts import render, redirect
from django.views.generic import ListView
from main.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView, UpdateView
from django.db.models import Q

def index(request):
    return render(request, 'index.html')

class KvizList(ListView):
    model = Kviz

class OsobaList(ListView):
    model = Osoba

class OdgovoriList(ListView):
    model = Odgovori

class PitanjaList(ListView):
    model = Pitanja

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:index")
		
	else:
		messages.error(request, "Unsuccessful registration. Invalid information.")
		form = NewUserForm()
        	
	return render (request=request, template_name="registration/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="registration/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("main:index")

class PretragaListView(ListView):
    model = Kviz
    template_name = 'kviz_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(imeKviza__icontains=query)
            )
        return queryset	

def unos_request(request):
	if request.method == "POST":
		form = KvizUnos(request.POST)
		if form.is_valid():
			form.save()
			messages.info(request, "Success.")
	else:
		form = KvizUnos()
		messages.error(request, "Invalid data.")
	return render(request, 'main/kviz_form.html', {'form': form})

def unoskandidat_request(request):
	if request.method == "POST":
		form = KandidatForm(request.POST)
		if form.is_valid():
			form.save()
			messages.info(request, "Success.")
	else:
		form = KandidatForm()
		messages.error(request, "Invalid data.")
	return render(request, 'main/kandidat_form.html', {'form': form})


class KandidatListView(ListView):
    model = Kandidat
    template_name = 'kandidati.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(ime__icontains=query) | Q(prezime__icontains=query)
            )
        return queryset

