from django.db import models
from django.utils import timezone
from .models import *
from datetime import datetime, timedelta


class PurchaseInvoiceItem(models.Model):
    id = models.AutoField(primary_key=True)
    no_pemasok = models.CharField(max_length=100, blank=True, null=True)  # a
    date = models.CharField(max_length=100, blank=True, null=True)  # b
    nama_pemasok = models.CharField(max_length=100, blank=True, null=True)  # c
    no_purchase_invoice = models.CharField(
        max_length=100, blank=True, null=True)  # e
    no_faktur_vendor = models.CharField(
        max_length=100, blank=True, null=True)  # f
    keterangan = models.CharField(max_length=100, blank=True, null=True)  # g
    no_akun_persediaan_barang = models.CharField(
        max_length=100, blank=True, null=True)  # h
    nama_akun_persediaan_barang = models.CharField(
        max_length=100, blank=True, null=True)  # i
    jumlah = models.CharField(max_length=100, blank=True, null=True)  # j
    id_barang = models.CharField(max_length=100, blank=True, null=True)  # k
    no_barang = models.CharField(max_length=100, blank=True, null=True)  # l
    keterangan_barang = models.CharField(
        max_length=100, blank=True, null=True)  # m
    qty = models.CharField(max_length=100, blank=True, null=True)  # n
    unit = models.CharField(max_length=100, blank=True, null=True)  # o

    def __str__(self):
        return f"{self.no_purchase_invoice}"

    def generate_json_all_data(self):
        data_to_summarize = {}
        for dt in PurchaseInvoiceItem.objects.all():
            key = dt.no_purchase_invoice;
            jumlah = dt.jumlah.replace(",","").replace(".","")
            item = {
                "itemId": dt.no_barang,  # k
                "description": dt.keterangan,  # m
                "qty": dt.qty,  # n
                "itemPrice": jumlah,  # j
                "unitCode": dt.unit,  # o
                "discount": "",  # null
                "discountId": "",  # null
                "taxId": ""  # null
            }
            expense = {
                "accountCode": dt.no_akun_persediaan_barang,  # h
                "description": dt.nama_akun_persediaan_barang,  # i
                "amount": jumlah  # j
            }
            if data_to_summarize.get(key) is None:
                data_to_summarize[key] = {
                    "no": key,  # e
                    "dt": dt.date,  # b
                    "locId": "164664240939100037530",  # static
                    "vendCode": dt.no_pemasok,  # a
                    "ptypeId": "HO164664374309602505821",  # static
                    "ptermId": "HO164664383888902573434",  # static
                    "userName": "WEB",  # static
                    "remark": dt.keterangan,  # G
                    "sourceTransId": "",  # null
                    "vendInvNo": dt.no_faktur_vendor,  # f
                    "items": [item],
                    "expenses": [expense],
                    "item_joined": 1,  # helper
                }
            else:
                data_to_summarize[key]["item_joined"] += 1
                data_to_summarize[key]["items"].append(item)
                data_to_summarize[key]["expenses"].append(expense)

        return data_to_summarize
