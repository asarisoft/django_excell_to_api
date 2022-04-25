from django.db import models
from django.utils import timezone
from .models import *
from datetime import datetime, timedelta


class Cashflow(models.Model):
    tgl_jv = models.CharField(max_length=100, blank=True, null=True) #a
    no_akun = models.CharField(max_length=100, blank=True, null=True) #b
    nama_akun = models.CharField(max_length=100, blank=True, null=True) #c
    catatan = models.CharField(max_length=100, blank=True, null=True) #d
    nilai_asing = models.CharField(max_length=100, blank=True, null=True) #e
    nama_dep = models.CharField(max_length=100, blank=True, null=True) #f
    nama_proyek = models.CharField(max_length=100, blank=True, null=True) #g
    no_jv = models.CharField(max_length=100, blank=True, null=True) #h
    bank_code = models.CharField(max_length=100, blank=True, null=True) #i
    nama_bank = models.CharField(max_length=100, blank=True, null=True) #j


def generate_json_all_data():
    data_to_summarize = {}
    for dt in Cashflow.objects.all():
        dt_detil = {
            "accountCode": dt.no_akun, #b
            "amount": dt.nilai_asing, #e
            "description": dt.catatan, #d
            "deptCode": dt.nama_dep, #f
            "prjCode": "" #null
        }
        if data_to_summarize.get(dt.no_jv) is None:
            data_to_summarize[dt.no_jv] = {
                "no": dt.no_jv, #H
                "dt": dt.tgl_jv, #A
                "type": "1", #st
                "locCode": "HO", #st
                "bankCode": dt.bank_code, #i
                "createBy": "retailsoft", #st
                "confirmBy": "retailsoft", #st
                "remark": "null", #null
                "referenceNo": "1", #static
                "bankIssuer": "2", #static
                "amount": dt.nilai_asing, #sum(e)
                "details": [dt_detil],
                "item_joined": 1,
                # "details": [{
                #     "accountCode": dt.no_akun, #b
                #     "amount": dt.nilai_asing, #e
                #     "description": dt.catatan, #d
                #     "deptCode": dt.nama_dep, #f
                #     "prjCode": "" #null
                # }]
            }
        else: 
            data_to_summarize[dt.no_jv]["item_joined"] += 1
            data_to_summarize[dt.no_jv]["amount"] += dt.nilai_asing
            data_to_summarize[dt.no_jv]["details"].append(dt_detil)

    return data_to_summarize

def save_to_json_data():
    datas = generate_json_all_data()
    # Save to db
  
# test
# from nxp.apps.cashflow.models import *
# generate_json_all_data