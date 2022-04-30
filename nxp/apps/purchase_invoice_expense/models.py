from django.db import models
from django.utils import timezone
from .models import *
from datetime import datetime, timedelta


class PurhaseInvoiceExpense(models.Model):
    class Meta:
        verbose_name_plural = "Cashflow"

    tgl_faktur = models.CharField(max_length=100, blank=True, null=True)  # a
    no_purchase_invoice = models.CharField(
        max_length=100, blank=True, null=True)  # b
    vendor_code = models.CharField(max_length=100, blank=True, null=True)  # c
    nama_pemasok = models.CharField(max_length=100, blank=True, null=True)  # d
    no_faktur_vendor = models.CharField(
        max_length=100, blank=True, null=True)  # f
    keterangan = models.CharField(max_length=100, blank=True, null=True)  # g
    no_akun_beban = models.CharField(max_length=100, blank=True, null=True)  # h
    nama_akun_beban = models.CharField(
        max_length=100, blank=True, null=True)  # i
    nilai_beban = models.CharField(max_length=100, blank=True, null=True)  # j
    item_id = models.CharField(max_length=100, blank=True, null=True)  # k
    item_name = models.CharField(
        max_length=100, blank=True, null=True)  # l
    qty = models.CharField(max_length=100, blank=True, null=True)  # m
    unit = models.CharField(max_length=100, blank=True, null=True)  # n

    def __str__(self):
        return f"{self.no_jv}"

        

    def generate_json_all_data(self):
        data_to_summarize = {}
        for dt in Cashflow.objects.all():
            key = no_purchase_invoice;
            nilai_beban = dt.jumlah.replace(",","").replace(".","")
            item = {
                "itemId": dt.item_id, #k 
                "description": dt.item_name, #l
                "qty": dt.qty, #m
                "itemPrice": nilai_beban, #j
                "unitCode": dt.unit, #n
                "discount": "",
                "discountId": "",
                "taxId": ""
            }
            expense = {
                "accountCode": dt.no_akun_beban, #h
                "description": dt.nama_akun_beban, #i
                "amount": dt.nilai_beban #j
            }
            if data_to_summarize.get(key) is None:
                nilai_assing = dt.nilai_asing.replace(".", "").replace(",", "")
                data_to_summarize[key] = {
                    "no": dt.no_purchase_invoice, #b
                    "dt": dt.tgl_faktur, #a
                    "locId": "164664240939100037530", #static
                    "vendCode": dt.vendor_code, #c
                    "ptypeId": "HO164664374309602505821", #static
                    "ptermId": "HO164664383888902573434", #static
                    "userName": "WEB", #static
                    "remark": dt.no_akun_beban, #h
                    "sourceTransId": "", #null
                    "vendInvNo": dt.no_faktur_vendor, #f
                    "items": [dt_detil],
                    "expenses": [dt_detil],
                    "item_joined": 1,  # helper
                }
            else:
                data_to_summarize[key]["item_joined"] += 1
                data_to_summarize[key]["items"].append(dt_detil)
                data_to_summarize[key]["expenses"].append(dt_detil)

        return data_to_summarize

# def save_to_json_data():
#     datas = generate_json_all_data()
    # Save to db

# test
# from nxp.apps.cashflow.models import *
# generate_json_all_data