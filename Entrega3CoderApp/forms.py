from django import forms

class Alumno_Formulario(forms.Form):
    alumno = forms.CharField(max_length=30)
    legajo = forms.CharField()
