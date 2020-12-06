from sapujagad.apps.contactus.models import Contactus
from django import forms


class ContactusForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = '__all__'

