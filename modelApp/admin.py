from django.contrib import admin
from modelApp.models import Persona


# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','email','telefono']


admin.site.register(Persona, PersonaAdmin)
