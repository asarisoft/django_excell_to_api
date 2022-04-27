import requests
import json
from urllib import response
from django.apps.registry import apps
from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from nxp.apps.user.decorators import login_validate
from nxp.backoffice.forms import LoginForm, UploadExcellForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from tablib import Dataset
from nxp.apps.cashflow.models import Cashflow
from nxp.apps.jsondata.models import JSONData

from nxp.apps.cashflow.admin import CashflowResource
from nxp.core.utils import save_to_json_data
from django.db.models import Sum

from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

get_model = apps.get_model


def login_view(request):
    auth_form = LoginForm(data=request.POST or None)
    if auth_form.is_valid():
        login(request, auth_form.get_user())
        auth_form.get_user()
        return redirect("backoffice:index")
    else:
        messages.error(request, "Username and Password are incorrect")

    list(messages.get_messages(request))
    context = dict(auth_form=auth_form,)
    return TemplateResponse(request, "backoffice/login.html", context)


def log_out(request):
    logout(request)
    return redirect("backoffice:login")


@login_validate
def index(request):
    return TemplateResponse(request, "backoffice/index.html")


@login_validate
def cashflow(request):
    datas = Cashflow.objects.all().order_by("-id")
    page = request.GET.get("page")
    search = request.GET.get("search", "")
    if search:
        datas = datas.filter(
            Q(no_akun__icontains=search) | Q(nama_akun__icontains=search) |
            Q(no_jv__icontains=search)
        )
    results_per_page = 30
    paginator = Paginator(datas, results_per_page)
    try:
        datas = paginator.get_page(page)
    except PageNotAnInteger:
        datas = paginator.get_page(1)
    except EmptyPage:
        datas = paginator.get_page(paginator.num_pages)

    if request.method == 'POST':
        resources = CashflowResource()
        new_datas = request.FILES['myfile']
        dataset = Dataset()
        imported_data = dataset.load(new_datas.read().decode(), format='csv')
        result = resources.import_data(
            dataset, dry_run=True)  # Test the data import
        print(result.has_errors())
        if not result.has_errors():
            # Actually import now
            resources.import_data(dataset, dry_run=False)

    context = {
        "datas": datas,
        "title": "Cashflow",
        "filter": {"search": search},
    }
    return TemplateResponse(request, "backoffice/cashflow/index.html", context)


@login_validate
def json_data(request):
    datas = JSONData.objects.all().order_by("-id")
    page = request.GET.get("page")

    model = request.GET.get("model", "Cashflow")
    datas = datas.filter(model=model)

    status = request.GET.get("status", "New")
    datas = datas.filter(status=status)

    search = request.GET.get("search", "")
    if search:
        datas = datas.filter(
            Q(key__icontains=search)
        )

    total_item = datas.aggregate(Sum('item_joined'))["item_joined__sum"]
    item_joined = datas.count()
    new_count = datas.filter(status="new").count()
    success_count = datas.filter(status="success").count()
    failed_count = datas.filter(status="failed").count()

    results_per_page = 30
    paginator = Paginator(datas, results_per_page)
    try:
        datas = paginator.get_page(page)
    except PageNotAnInteger:
        datas = paginator.get_page(1)
    except EmptyPage:
        datas = paginator.get_page(paginator.num_pages)

    context = {
        "datas": datas,
        "title": "JSON DATA",
        "filter": {
            "search": search,
            "status": status,
            "model": model,
        },
        "total_item": total_item,
        "item_joined": item_joined,
        "new_count": new_count,
        "success_count": success_count,
        "failed_count": failed_count
    }
    return TemplateResponse(request, "backoffice/json_data/index.html", context)


# for every model to generate json data 
def generate_json_data(request):
    app = request.GET.get("app")
    model = request.GET.get("model")
    save_to_json_data(app, model)
    return JsonResponse({"message": "Success"}, status=200)


# process data to server
@csrf_exempt
def process_data(request):
    model = request.GET.get("model")
    key = request.GET.get("key")
    status = request.GET.get("status", "")
    qs = JSONData.objects.filter(model=model).order_by('-id')
    if key:
        qs = qs.filter(key=key)
    else:
        qs = qs.filter(status=status)
    qs = qs.first()
    if qs:
        response = send_to_server(model, qs)
    else:
        response = {"status": "error", "data": {"message": "no data found"}}
    
    print("RESPOSSSS", response)
    if response["status"] == "success":
        qs.status="success"
        qs.response=response["data"]
        qs.save()
        return JsonResponse(response, status=200)
    else: 
        if qs:
            qs.status="failed"
            qs.response=response["data"]
            qs.save()
        return JsonResponse(response, status=400)


def send_to_server(model, data):
    url = f"https://finance.cakap.com/cakap_trn/api/{model.lower()}/savetrans/"
    print(url)
    payload = {
        "doc": data.json_data
    }
    print(payload)
    headers = {
        'usr': 'admin',
        'token': 'AmeZqgA4ogPXKQT9EXjpyQRtqDT2ngrd',
        'content-type': 'application/x-www-form-urlencoded'
    }
    request = requests.post(url, payload, headers=headers)
    response = request.json()
    print(response)
    if response["status"] == 200:
        return {"status": "success", "data": response}
    else:
        return {"status": "failed", "body": payload, "data": response}
        
