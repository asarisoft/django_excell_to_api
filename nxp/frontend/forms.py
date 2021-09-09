from django import forms

from nxp.apps.dealer.models import Dealer
from nxp.apps.reward.models import Balance, Scan, Redeem
from nxp.apps.user.models import User
from nxp.apps.serial_number.models import SerialNumber


class ScanForm(forms.Form):
    serial_number = forms.CharField()
    dealer_code = forms.CharField(required=False)
    product = forms.CharField()
    mobile_number = forms.CharField()
    name = forms.CharField()
    dealer_name = forms.CharField(required=False)
    dealer_address = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(ScanForm, self).__init__(*args, **kwargs)
        self.serial_number = 0
    
    def clean_serial_number(self):
        serial_number = self.cleaned_data.get("serial_number", False)
        serial = SerialNumber.objects.filter(serial_number=serial_number).first()
        if not serial:
            raise forms.ValidationError("QR CODE tidak ditemukan")
        elif serial.status == 'redeem':
            raise forms.ValidationError("QR CODE sudah digunakan")
        
        self.serial_number = serial
        return serial_number

    # def clean_dealer_code(self):
    #     code = self.cleaned_data.get("dealer_code", False)
    #     if code and not Dealer.objects.filter(code=code).first():
    #         raise forms.ValidationError("Kode Dealer tidak ditemukan")
    #     return code

    def clean(self):
        cleaned_data = super(ScanForm, self).clean()
        if self.errors:
            return cleaned_data
        # serial_number = self.cleaned_data['serial_number']
        # dealer_code = self.cleaned_data['dealer_code']
        # if serial_number[0].lower() == 'd':
        #     if not dealer_code:
        #         raise forms.ValidationError("Kode dealer wajib diisi untuk qrcode ini")
        #     elif not Dealer.objects.filter(code=dealer_code).first():
        #         raise forms.ValidationError("Kode Dealer tidak ditemukan")
        return cleaned_data

    def save(self):
        data = self.cleaned_data
        user, _ = User.objects.update_or_create(
            mobile_number = data['mobile_number'],
            username = data['mobile_number'],
            defaults = {
                "name" : data['name'],
                "dealer_name" : data['dealer_name'], 
                "dealer_address" : data['dealer_address'], 
            }
        )
        scan = Scan(
            serial_number=self.serial_number, 
            dealer_code=data['dealer_code'],
            product=data['product'], 
            user=user,
        )
        scan.save()
        SerialNumber.objects.filter(
            serial_number=scan.serial_number).update(status='redeem')
        return scan


class RedeemForm(forms.Form):
    mobile_number = forms.CharField()
    nominal_value = forms.IntegerField()
    wallet_type = forms.CharField()
    dealer_code = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(RedeemForm, self).__init__(*args, **kwargs)
        self.user = None
    
    def clean_nominal_value(self):
        nominal_value = self.cleaned_data['nominal_value']
        if nominal_value < 10000:
            raise forms.ValidationError("Nominal minimal Rp. 10.000")
        
        if not (nominal_value % 1000 == 0):
            raise forms.ValidationError("Nominal harus kelipatan 1.000")
        return nominal_value

    # def clean_dealer_code(self):
    #     code = self.cleaned_data.get("dealer_code", False)
    #     if code and not Dealer.objects.filter(code=code).first():
    #         raise forms.ValidationError("Kode Dealer tidak ditemukan")
    #     return code

    def clean(self):
        cleaned_data = super(RedeemForm, self).clean()
        if self.errors:
            return cleaned_data

        nominal_value = self.cleaned_data['nominal_value']
        self.user = User.objects.filter(
            mobile_number = self.cleaned_data['mobile_number'],
        ).first()

        if not self.user:
            raise forms.ValidationError("User tidak ditemukan")

        balance = Balance.objects.filter(user=self.user).order_by('-id').first()
        if balance.balance < nominal_value:
            raise forms.ValidationError("Saldo anda tidak cukup")
        
        return cleaned_data

    def save(self):
        data = self.cleaned_data
        redeem = Redeem.objects.create(
            user = self.user,
            wallet_type = data['wallet_type'],
            value = data['nominal_value'],
            dealer_code = data['dealer_code']
        )
        return redeem
