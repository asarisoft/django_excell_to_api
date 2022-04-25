from django.db import models
from django.utils import timezone
from .models import *
from datetime import datetime, timedelta


class Sales(models.Model)
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


def generate_json_all_date():
    data_to_summarize 
    for dt in Sales.objects.all()
    return  {
        "no": no_jv, #H
        "dt": tgl_jv, #A
        "type": "1", #st
        "locCode": "HO", #st
        "bankCode": bank_code, #i
        "createBy": "retailsoft", #st
        "confirmBy": "retailsoft", #st
        "remark": "null", #null
        "referenceNo": "1", #static
        "bankIssuer": "2", #static
        "amount": nilai_asing, #sum(e)
        "details": [{
            "accountCode": no_akun, #b
            "amount": nilai_asing, #e
            "description": catatan, #d
            "deptCode": nama_dep, #f
            "prjCode": "" #null
        }]
    }	
  