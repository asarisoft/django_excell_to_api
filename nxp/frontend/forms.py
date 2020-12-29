from django import forms

from nxp.apps.dealer.models import Dealer
from nxp.apps.formulir.models import Formulir
from nxp.apps.product.models import Product


class FormulirForm(forms.ModelForm):
    class Meta:
        model = Formulir
        fields = "__all__"
        exclude = ("status",)

    def clean_dealer_code(self):
        code = self.cleaned_data.get("dealer_code", False)
        if not Dealer.objects.filter(code=code).first():
            raise forms.ValidationError("Kode Dealer tidak ditemukan")
        return code

    def clean_serial_number(self):
        serial_number = self.cleaned_data.get("serial_number", False)
        if not Product.objects.filter(serial_number=serial_number).first():
            raise forms.ValidationError("Serial Number tidak ditemukan")
        if Formulir.objects.filter(serial_number=serial_number).first():
            raise forms.ValidationError("Serial Number sudah digunakan")
        return serial_number
