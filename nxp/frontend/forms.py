from nxp.apps.formulir.models import Formulir
from django import forms

class FormulirForm(forms.ModelForm):
    class Meta:
        model = Formulir
        fields = '__all__'
