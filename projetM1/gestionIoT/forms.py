from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Proprietaire, Reseau
from django_countries.widgets import CountrySelectWidget
#from phonenumber_field.formfields import PhoneNumberField

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

     
class ReseauForm(ModelForm):
    class Meta:
        model = Reseau
        fields = ['description_reseau', 'nom_reseau']
        labels = {'nom_reseau':('Nom du réseau'),'description_reseau':('Description du réseau')}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Sauvegarder'))


######################

class UserForm1(ModelForm):
    class Meta:
        model = User
        fields = ['username', 
            'first_name', 
            'last_name', 
            'email', 
            'password'
        ]
        labels = {'username':('Nom d\'utilisateur'), 
            'first_name':('Votre prénom'),  
            'last_name':('Votre nom de famille'),
            'mail':('Votre adresse mail'), 
            'password':('Mot de passe')
        }
        widgets ={'password': forms.PasswordInput}

class ProprietaireForm1(ModelForm):
    class Meta:
        model = Proprietaire
        fields = ['telephone_proprio', 
            'pays_proprio', 
            'avatar'
        ]
        labels = {'telephone_proprio':('Numéro de téléphone'), 
            'pays_proprio':('Nationalité'), 
            'avatar':('Entrer une photo de profil')
        }
        widgets = {'pays_proprio': CountrySelectWidget()} #, 'telephone_proprio': PhoneNumberPrefixWidget()}

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur",max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

