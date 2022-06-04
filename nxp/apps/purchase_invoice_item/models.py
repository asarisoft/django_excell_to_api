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
        max_length=100, blank=True, null=True)  # d
    no_faktur_vendor = models.CharField(
        max_length=100, blank=True, null=True)  # e
    keterangan = models.CharField(max_length=100, blank=True, null=True)  # f
    no_akun_persediaan_barang = models.CharField(
        max_length=100, blank=True, null=True)  # g
    nama_akun_persediaan_barang = models.CharField(
        max_length=100, blank=True, null=True)  # h
    jumlah = models.CharField(max_length=100, blank=True, null=True)  # i
    id_barang = models.CharField(max_length=100, blank=True, null=True)  # j
    no_barang = models.CharField(max_length=100, blank=True, null=True)  # k
    keterangan_barang = models.CharField(
        max_length=100, blank=True, null=True)  # l
    qty = models.CharField(max_length=100, blank=True, null=True)  # m
    unit = models.CharField(max_length=100, blank=True, null=True)  # n
    item_price = models.CharField(max_length=100, blank=True, null=True)  # o

    def __str__(self):
        return f"{self.no_purchase_invoice}"

    def generate_json_all_data(self):
        data_to_summarize = {}
        for dt in PurchaseInvoiceItem.objects.all():
            key = dt.no_purchase_invoice;
            jumlah = dt.jumlah.replace(",","").replace(".","")
            item = {
                "itemId": dt.id_barang or "",  # j
                "description": dt.keterangan or "",  # l
                "qty": dt.qty or "",  # m
                "itemPrice": dt.item_price or "",  # o
                "unitCode": dt.unit or "",  # n
                "discount": "",  # null
                "discountId": "",  # null
                "taxId": ""  # null
            }
            expense = {
                "accountCode": dt.no_akun_persediaan_barang or "",  # g
                "description": dt.nama_akun_persediaan_barang or "",  # h
                "amount": jumlah or ""  # i
            }
            if data_to_summarize.get(key) is None:
                data_to_summarize[key] = {
                    "no": key,  # d
                    "dt": f"{dt.date} 00:00:00",  # b
                    "locId": "164664240939100037530",  # static
                    "vendCode": dt.no_pemasok or "",  # a
                    "ptypeId": "HO164664374309602505821",  # static
                    "ptermId": "HO164664383888902573434",  # static
                    "userName": "admin",  # static
                    "remark": dt.keterangan or "",  # f
                    "sourceTransId": "",  # null
                    "vendInvNo": dt.no_faktur_vendor or "",  # e
                    "items": [item],
                    "expenses": [expense],
                    "item_joined": 1,  # helper
                }
            else:
                data_to_summarize[key]["item_joined"] += 1
                data_to_summarize[key]["items"].append(item)
                data_to_summarize[key]["expenses"].append(expense)

        return data_to_summarize
