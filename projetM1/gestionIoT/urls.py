from django.contrib import admin
from django.urls import path, include
from . import views

"""from .views import (ProprietaireListView, 
    ProprietaireCreateView, 
    ProprietaireUpdateView, 
    #UserCreateView,
    #ReseauCreateView,
    ReseauListView,
    #ReseauUpdateView,
    #LoginUser,
)"""

# On import les vues de Django, avec un nom spécifique
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accueil', views.home, name='accueil'),
    path('connexion', views.LoginUser.as_view(), name='connexion'),
    path('deconnexion', views.deconnexion, name='deconnexion'),
    path('nouveau_reseau', views.nouveau_reseau, name='nouveau_reseau'),
    path('inscription', views.inscription, name="inscription"),

    path('mon_profil', views.mon_profil),
    path('', views.home1),
    path('accounts/', include('django.contrib.auth.urls')),
    path('mes_reseau', views.liste_reseau, name='reseau_list'),

] 

""" accounts/login/ [name='login']
    accounts/logout/ [name='logout']
    accounts/password_change/ [name='password_change']
    accounts/password_change/done/ [name='password_change_done']
    accounts/password_reset/ [name='password_reset']
    accounts/password_reset/done/ [name='password_reset_done']
    accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    accounts/reset/done/ [name='password_reset_complete']
 """