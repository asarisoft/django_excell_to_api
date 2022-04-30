from django.db import models
from django.utils import timezone
from .models import *
from datetime import datetime, timedelta


class Invoice(models.Model):
    tgl_faktur = models.CharField(max_length=100, blank=True, null=True)  # a
    no_pelanggan = models.CharField(max_length=100, blank=True, null=True)  # b
    id_pelanggan = models.CharField(max_length=100, blank=True, null=True)  # c
    nama_pelanggan = models.CharField(
        max_length=100, blank=True, null=True)  # d
    no_faktur = models.CharField(max_length=100, blank=True, null=True)  # e
    keterangan = models.CharField(max_length=250, blank=True, null=True)  # f
    id_barang = models.CharField(max_length=100, blank=True, null=True)  # g
    no_barang = models.CharField(max_length=100, blank=True, null=True)  # h
    keterangan_barang = models.CharField(
        max_length=100, blank=True, null=True)  # i
    kuantitas = models.CharField(max_length=100, blank=True, null=True)  # j
    jumlah = models.CharField(max_length=100, blank=True, null=True)  # k

    def __str__(self):
        return f"{self.nama_pelanggan}"

    def generate_json_all_date(self):
        data_to_summarize = {}
        for dt in Invoice.objects.all():
            jumlah = dt.jumlah.replace(".", "").replace(",","")
            item = {
                "itemId": dt.id_barang,  # G
                "itemCode": dt.no_barang,  # H
                "description": dt.keterangan_barang,  # I
                "qty": dt.kuantitas,  # J
                "itemPrice": jumlah,  # K
                "discount": "0",  # null
                "discountId": "",  # null
                "taxId": ""  # static
            }

            payment = {
                "ptypeId": "FC01155920071225100011937",  # static
                "ptermId": "",  # stati
                "voucherId": "",  # static
                "paymentAmount": jumlah,  # K
                "bankIssuer": "",  # null
                "referenceNo": "",  # null
                "approvalNo": "",  # null
                "traceNo": "",  # null
                "terminalId": ""  # null
            }

            if data_to_summarize.get(dt.nama_pelanggan) is None:
                {
                    "no": dt.nama_pelanggan,  # D
                    "dt": dt.tgl_faktur,  # A
                    "locId": "FC01156274702276500063818",  # static
                    "custId": dt.id_pelanggan,  # C
                    "ptypeId": "",  # static
                    "ptermId": "",  # static
                    "cashier": "Topup Cashier 1",  # static
                    "remark": dt.keterangan,  # F
                    "sourceTransId": "",  # null
                    "items": [item],
                    "payments": [payment],
                    "item_joined": 1,  # helper
                }
            else:
                data_to_summarize[dt.nama_pelanggan]["item_joined"] += 1
                data_to_summarize[dt.nama_pelanggan]["items"].append(item)
                data_to_summarize[dt.nama_pelanggan]["payments"].append(payment)

        return data_to_summarize
