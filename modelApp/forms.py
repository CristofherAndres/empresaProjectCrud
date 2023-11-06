from django import forms
from modelApp.models import Persona, Estado
from django.core import validators

#Actualizar el dato
class PersonaForm(forms.Form):

    """ ESTADOS PARA UN SELECT """
    ESTADOS = [('disponible','DISPONIBLE'), ('no disponible','NO DISPONIBLE')]

    nombre      = forms.CharField(max_length=50)
    telefono    = forms.CharField(max_length=12)
    email       = forms.CharField(max_length=50)
    """ Estado sera desde la tabla estados con la FK """
    estado      = forms.ModelChoiceField(queryset=Estado.objects.all())

    nombre.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-select'

#Crear el dato y almacenarlo en la DB
class PersonaForm(forms.ModelForm):
    """ ESTADOS PARA UN SELECT """
    ESTADOS = [('DISPONIBLE','DISPONIBLE'), ('NO DISPONIBLE','NO DISPONIBLE')]

    nombre      = forms.CharField(max_length=50, 
                validators=[
                    validators.MinLengthValidator(2),
                    validators.MaxLengthValidator(15)
                ]
    )
    telefono    = forms.CharField(max_length=12, required=False)
    email       = forms.CharField(max_length=50)
    estado      = forms.ModelChoiceField(queryset=Estado.objects.all())


    def clean_email(self):
        input_email = self.cleaned_data['email']
        if input_email.find('@') == -1:
            raise forms.ValidationError('Ingrese un correo valido, tiene que tener un @')
        return input_email


    nombre.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-select'


    class Meta:
        model = Persona
        fields = '__all__'