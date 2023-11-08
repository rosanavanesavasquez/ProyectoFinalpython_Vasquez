from django import forms


class AuditorFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField()


class SectorForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    UAP = forms.CharField(max_length=5, initial='Todas')  
    UAT = forms.CharField(max_length=5, initial='Todas')