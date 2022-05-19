from datetime import datetime, timedelta
from .models import *
from django.utils import timezone
from django.db import models

# Create your models here.
class JV(models.Model):
    id = models.AutoField(primary_key=True)
    no_jv = models.CharField(max_length=100, blank=True, null=True)  # a
    no_akun = models.CharField(max_length=100, blank=True, null=True)  # b
    tgl_jv = models.CharField(max_length=100, blank=True, null=True)  # c
    nama_akun = models.CharField(
        max_length=100, blank=True, null=True)  # d
    keterangan = models.CharField(max_length=100, blank=True, null=True)  # e
    debit = models.CharField(max_length=250, blank=True, null=True)  # f
    kredit = models.CharField(max_length=100, blank=True, null=True)  # g
    nama_dep = models.CharField(max_length=100, blank=True, null=True)  # h

    def __str__(self):
        return f"{self.no_jv}"

    def generate_json_all_data(self):
        data_to_summarize = {}
        for dt in JV.objects.all():
            key = dt.no_jv
            debit = dt.debit.replace(".", "").replace(",","")
            kredit = dt.kredit.replace(".", "").replace(",","")
            detil = {
                "accountCode": dt.no_akun,  # B
                "debit": int(debit),  # F
                "credit": int(kredit),  # G
                "currencyCode": "IDR",  # static
                "currencyRate": 1,  # static
                "description": dt.keterangan,  # E
                "locCode": "HO",  # static
                "deptCode": dt.nama_dep,  # H
                "prjCode": ""  # null
            }
            if data_to_summarize.get(key) is None:
                data_to_summarize[key]={
                    "no": key,  # A
                    "dt": f"{dt.tgl_jv} 00:00:00",  # C
                    "reviewDate": f"{dt.tgl_jv} 00:00:00",  # C
                    "approveddDate": f"{dt.tgl_jv} 00:00:00",  # C
                    "type": "1",  # static
                    "locCode": "HO",  # static
                    "createBy": "admin",  # static
                    "reviewedBy": "admin",  # static
                    "approvedBy": "admin",  # static
                    "remark": "",  # E
                    "details": [detil],
                    "item_joined": 1,  # helper
                }
            else:
                data_to_summarize[key]["item_joined"] += 1
                data_to_summarize[key]["details"].append(detil)
        print(data_to_summarize)
        return data_to_summarize
