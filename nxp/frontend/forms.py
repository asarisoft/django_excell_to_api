from django import forms

from nxp.apps.dealer.models import Dealer
from nxp.apps.reward.models import Scan
from nxp.apps.user.models import User
from nxp.apps.serial_number.models import SerialNumber


class ScanForm(forms.Form):
    serial_number = forms.CharField()
    dealer_code = forms.CharField(required=False)
    product = forms.CharField()
    mobile_number = forms.CharField()
    name = forms.CharField()
    
    def clean_serial_number(self):
        serial_number = self.cleaned_data.get("serial_number", False)
        serial = SerialNumber.objects.filter(serial_number=serial_number)
        if not serial.first():
            raise forms.ValidationError("Serial Number tidak ditemukan")
        elif serial.first().status == 'redeem':
            raise forms.ValidationError("Serial Number sudah digunakan")
        return serial_number

    def clean_dealer_code(self):
        code = self.cleaned_data.get("dealer_code", False)
        if code and not Dealer.objects.filter(code=code).first():
            raise forms.ValidationError("Kode Dealer tidak ditemukan")
        return code

    def clean(self):
        cleaned_data = super(ScanForm, self).clean()
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

    def save(self):
        data = self.cleaned_data
        user, _ = User.objects.update_or_create(
            mobile_number = data['mobile_number'],
            username = data['mobile_number'],
            defaults = {
                "name" : data['name'],
            }
        )
        scan = Scan(serial_number=data['serial_number'], dealer_code=data['dealer_code'],
            product=data['product'], user=user)
        scan.save()
        SerialNumber.objects.filter(
            serial_number=scan.serial_number).update(status='redeem')
