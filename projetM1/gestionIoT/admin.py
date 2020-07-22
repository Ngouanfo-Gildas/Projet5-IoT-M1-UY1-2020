from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Proprietaire #, Reseau

admin.site.register(Proprietaire)
#admin.site.register(Reseau)