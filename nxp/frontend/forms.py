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

    def clean_serial_number(self):
        serial_number = self.cleaned_data.get("serial_number", False)
        serial = SerialNumber.objects.filter(serial_number=serial_number)
        if not serial.first():
            raise forms.ValidationError("Serial Number tidak ditemukan")
        elif serial.first().status == 'redeem':
            raise forms.ValidationError("Serial Number sudah digunakan")
        return serial_number

    #  def clean_dealer_code(self):
    #     code = self.cleaned_data.get("dealer_code", False)
    #     if code and not Dealer.objects.filter(code=code).first():
    #         raise forms.ValidationError("Kode Dealer tidak ditemukan")
    #     return code

    def clean(self):
        cleaned_data = super(FormulirForm, self).clean()
        if self.errors:
            return cleaned_data

        serial_number = self.cleaned_data['serial_number']
        dealer_code = self.cleaned_data['dealer_code']
        if serial_number[0].lower() == 'd':
            if not dealer_code:
                raise forms.ValidationError("Kode dealer wajib diisi untuk qrcode ini")
            elif not Dealer.objects.filter(code=dealer_code).first():
                raise forms.ValidationError("Kode Dealer tidak ditemukan")

        return cleaned_data

    def save(self, commit=True):
        formulir = super(FormulirForm, self).save()
        SerialNumber.objects.filter(serial_number=formulir.serial_number).update(status='redeem')
        return formulir
