from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *

from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

from django.contrib.auth import authenticate , logout


@login_required(redirect_field_name='connexion')
def nouveau_reseau(request):
    save = False
    form = ReseauForm(request.POST or None)
    if request.method  == 'POST':
        reseau = Reseau()
        user = User()
        propr = Proprietaire()
        if form.is_valid(): 
            nom_reseau = form.cleaned_data['nom_reseau']
            description_reseau = form.cleaned_data['description_reseau']
            
            reseau = form.save(commit=False)
            if user.is_authenticated:
                reseau.proprietaire_id = request.user.id
            #reseau.proprietaire_id = 1 #Proprietaire.objects.filter(user = 1)
            
            reseau.save()
            save = True
            return redirect('reseau_list')
    return render(request, 'gestionIoT/nouveau_reseau.html', {'form':form })

@login_required(redirect_field_name='connexion')
def liste_reseau(request):
    user = User()
    reseau = Reseau()
    nb = 0
    if user.is_authenticated:
        #reseau.proprietaire_id = request.user.id
        reseaux = Reseau.objects.filter(proprietaire_id = request.user.id)
        
    return render(request, 'gestionIoT/reseau_list.html', {'reseaux': reseaux, "nb": nb}) #locals())

def home(request):
    return render(request, 'gestionIoT/accueil.html', locals())

def home1(request):
    return render(request, 'gestionIoT/accueil1.html', locals())


def inscription(request):
    save = False
    form = UserForm1(request.POST or None)
    form1 = ProprietaireForm1(request.POST or None, request.FILES)
    if request.method  == 'POST':
        proprietaire = Proprietaire()
        user = User()
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = form.save(commit=False)
            user.set_password(password)
            user.save()

            """
            proprietaire.telephone_proprio = form1.cleaned_data['telephone_proprio']
            proprietaire.pays_proprio = form1.cleaned_data['pays_proprio']
            ville_proprio = form1.cleaned_data['ville_proprio']
            avatar = form1.cleaned_data['avatar'] """
            
            # proprietaire.user_id = user.id
            proprietaire = form1.save(commit=False)
            proprietaire.user = user
            proprietaire.save()
            save = True
            return redirect('connexion')
    return render(request, 'gestionIoT/inscription.html', {'form':form, 'form1':form1})


class LoginUser(LoginView):
    model = User
    fields = ['username', 'password']
    template_name = "gestionIoT/login.html"


def deconnexion(request):
    logout(request)
    return redirect(home)

@login_required(redirect_field_name='connexion')
def mon_profil(request):
    user = User()
    if user.is_authenticated:
        reseaux = Reseau.objects.filter(proprietaire_id = request.user.id)
        proprietaire = Proprietaire.objects.filter(user_id = request.user.id)
        #print(proprietaire.telephone_proprio)
    return render(request, 'gestionIoT/votre_profil.html', {"reseaux": reseaux, "proprietaire": proprietaire})

@login_required(redirect_field_name='login')
def capteur(request, id_reseau):
    user = User()
    if user.is_authenticated:
        reseaux = Reseau.objects.filter(proprietaire_id = request.user.id)
        proprietaire = Proprietaire.objects.filter(user_id = request.user.id)
        #print(proprietaire.telephone_proprio)
    return render(request, 'gestionIoT/votre_profil.html', 
    {"reseaux": reseaux, "proprietaire": proprietaire})

def nouveau_puits(request):
    pass

def edit_reseau(request):
    pass

def delete_reseau(request):
    pass

############################################################################################
##########                   gestion des capteurs et des données                  ##########
#############----------------------------------------------------------------###############

import json
import os, sys, stat
import shutil

#print(os.getcwd())
#print(os.listdir('.'))
