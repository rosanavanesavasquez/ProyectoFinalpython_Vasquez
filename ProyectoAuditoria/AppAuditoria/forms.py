from django import forms
from .models import Sector
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AuditorFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField()


class SectorForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    UAP = forms.CharField(max_length=5, initial='Todas')  
    UAT = forms.CharField(max_length=5, initial='Todas')
    
class Meta:
        model = Sector
        fields = ['nombre', 'UAP','UAT']
    
class UserRegisterForm(UserCreationForm):

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
   
    #last_name = forms.CharField()
    #first_name = forms.CharField()
    #imagen_avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    #Acá se definen las opciones que queres modificar del usuario, 
    #Ponemos las básicas
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 


    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}