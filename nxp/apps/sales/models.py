from django.db import models
from django.utils import timezone
from .models import *
from datetime import datetime, timedelta


class Sales(models.Model)
    tgl_faktur = models.CharField(max_length=100, blank=True, null=True) #a
    no_pelanggan = models.CharField(max_length=100, blank=True, null=True) #b
    id_pelanggan = models.CharField(max_length=100, blank=True, null=True) #c
    nama_pelanggan = models.CharField(max_length=100, blank=True, null=True) #d
    no_faktur = models.CharField(max_length=100, blank=True, null=True) #e
    keterangan = models.CharField(max_length=100, blank=True, null=True) #f
    id_barang = models.CharField(max_length=100, blank=True, null=True) #g
    no_barang = models.CharField(max_length=100, blank=True, null=True) #h
    keterangan_barang = models.CharField(max_length=100, blank=True, null=True) #i
    kuantitas = models.CharField(max_length=100, blank=True, null=True) #j
    jumlah = models.CharField(max_length=100, blank=True, null=True) #k


def generate_json_all_date(self):
    
    return  {
        "no": "TOP/01/19091618/0116", d
        "dt": "2019-09-16T18:18:04+07:00", a
        "locId": "FC01156274702276500063818",
        "custId": "FC01155426042883008870797",
        "ptypeId": "",
        "ptermId": "",
        "cashier": "Topup Cashier 1",
        "remark": "",
        "sourceTransId": "",
        "items": [{
            "itemId": "",
            "itemCode": "TOPUP",
            "description": "",
            "qty": 1,
            "itemPrice": "7999999",
            "discount": "0",
            "discountId": "",
            "taxId": ""
        }],
        "payments": [{
            "ptypeId": "FC01155920071225100011937",
            "ptermId": "",
            "voucherId": "",
            "paymentAmount": "7999999",
            "bankIssuer": "",
            "referenceNo": "",
            "approvalNo": "",
            "traceNo": "",
            "terminalId": ""
            }
        ]}
