from django import forms

class MenuFormulario(forms.Form):
    categoria = forms.CharField()
    descripcion = forms.CharField()
    precio = forms.FloatField()
    disponible = forms.BooleanField()

class BuscaMenuForm(forms.Form):
    descripcion = forms.CharField()
