from django import forms

from nxp.apps.dealer.models import Dealer
from nxp.apps.formulir.models import Formulir
from nxp.apps.product.models import Product
from nxp.apps.serial_number.models import SerialNumber


class FormulirForm(forms.ModelForm):
    dealer_code = forms.CharField(required=False)

    class Meta:
        model = Formulir
        fields = "__all__"
        exclude = ("status",)

    def clean_dealer_code(self):
        code = self.cleaned_data.get("dealer_code", False)
        if code and not Dealer.objects.filter(code=code).first():
            raise forms.ValidationError("Kode Dealer tidak ditemukan")
        return code

    def clean_serial_number(self):
        serial_number = self.cleaned_data.get("serial_number", False)
        serial = SerialNumber.objects.filter(serial_number=serial_number)
        if not serial.first():
            raise forms.ValidationError("Serial Number tidak ditemukan")
        elif serial.status == 'redeem':
            raise forms.ValidationError("Serial Number sudah digunakan")
        return serial_number
