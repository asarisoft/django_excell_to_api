from django.db import models
from django.utils import timezone
from .models import *
from datetime import datetime, timedelta


class Cashflow(models.Model):
    class Meta:
        verbose_name_plural = "Cashflow"
    id = models.AutoField(primary_key=True)
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
    type = models.CharField(max_length=100, blank=True, null=True) #k

    def __str__(self):
        return f"{self.no_jv}"

    def generate_json_all_data(self):
        data_to_summarize = {}
        for dt in Cashflow.objects.all():
            nilai_assing = dt.nilai_asing.replace(".", "").replace(",","")
            dt_detil = {
                "accountCode": dt.no_akun, #b
                "amount": int(nilai_assing), #e
                "description": dt.nama_akun, #c
                "deptCode": dt.nama_dep, #f
                "prjCode": "" #null
            }
            if data_to_summarize.get(dt.no_jv) is None:
                data_to_summarize[dt.no_jv] = {
                    "no": dt.no_jv, #H
                    "dt": f"{dt.tgl_jv} 00:00:00", #A
                    "type": dt.type, #st
                    "locCode": "HO", #st
                    "bankCode": dt.bank_code, #i
                    "createBy": "admin", #st
                    "confirmBy": "admin", #st
                    "remark": dt.catatan, #d
                    "referenceNo": "0", #static
                    "bankIssuer": "0", #static
                    "amount": int(nilai_assing), #sum(e)
                    "details": [dt_detil],                    
                    "item_joined": 1, #helper
                }
            else: 
                data_to_summarize[dt.no_jv]["item_joined"] += 1
                data_to_summarize[dt.no_jv]["amount"] += int(nilai_assing)
                data_to_summarize[dt.no_jv]["details"].append(dt_detil)

        return data_to_summarize

# def save_to_json_data():
#     datas = generate_json_all_data()
    # Save to db
  
# test
# from nxp.apps.cashflow.models import *
# generate_json_all_data