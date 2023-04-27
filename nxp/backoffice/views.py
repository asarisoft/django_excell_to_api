import os
import mimetypes
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
from nxp.apps.jsondata.models import JSONData
from nxp.apps.purchase_invoice_item.models import PurchaseInvoiceItem
from nxp.apps.purchase_invoice_item.admin import PurchaseInvoiceItemResources

from nxp.apps.purchase_invoice_expense.models import PurchaseInvoiceExpense
from nxp.apps.purchase_invoice_expense.admin import PurchaseInvoiceExpenseResources

from nxp.apps.cashflow.models import Cashflow
from nxp.apps.cashflow.admin import CashflowResource

from nxp.apps.jv.models import JV
from nxp.apps.jv.admin import JVResources
from nxp.apps.invoice.models import Invoice
from nxp.apps.invoice.admin import InvoiceResources
from nxp.apps.lastkey.models import LastKey
from nxp.apps.settings.models import Settings

from nxp.core.utils import save_to_json_data
from django.db.models import Sum

from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

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
def purchase_invoice_item(request):
    datas = PurchaseInvoiceItem.objects.all().order_by("-id")
    page = request.GET.get("page")
    search = request.GET.get("search", "")
    if search:
        datas = datas.filter(
            Q(no_purchase_invoice__icontains=search)
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
        resources = PurchaseInvoiceItemResources()
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
        "title": "Purchase Invoice Item",
        "filter": {"search": search},
    }
    return TemplateResponse(
        request, "backoffice/purchase_inv_item/index.html", context)


@login_validate
def purchase_invoice_expense(request):
    datas = PurchaseInvoiceExpense.objects.all().order_by("-id")
    page = request.GET.get("page")
    search = request.GET.get("search", "")
    if search:
        datas = datas.filter(
            Q(no_purchase_invoice__icontains=search)
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
        resources = PurchaseInvoiceExpenseResources()
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
        "title": "Purchase Invoice Expense",
        "filter": {"search": search},
    }
    return TemplateResponse(
        request, "backoffice/purchase_inv_expense/index.html", context)


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
def jv(request):
    datas = JV.objects.all().order_by("-id")
    page = request.GET.get("page")
    search = request.GET.get("search", "")
    if search:
        datas = datas.filter(
            Q(nama_pelanggan__icontains=search)
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
        resources = JVResources()
        new_datas = request.FILES['myfile']
        dataset = Dataset()
        imported_data = dataset.load(new_datas.read().decode(), format='csv')
        result = resources.import_data(
            dataset, dry_run=True)  # Test the data import
        if not result.has_errors():
            # Actually import now
            resources.import_data(dataset, dry_run=False)

    context = {
        "datas": datas,
        "title": "JV",
        "filter": {"search": search},
    }
    return TemplateResponse(request, "backoffice/jv/index.html", context)


@login_validate
def invoice(request):
    datas = Invoice.objects.all().order_by("-id")
    page = request.GET.get("page")
    search = request.GET.get("search", "")
    if search:
        datas = datas.filter(
            Q(nama_pelanggan__icontains=search)
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
        resources = InvoiceResources()
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
        "title": "Invoice",
        "filter": {"search": search},
    }
    return TemplateResponse(request, "backoffice/invoice/index.html", context)


@login_validate
def json_data(request):
    datas = JSONData.objects.all().order_by("-id")
    page = request.GET.get("page")

    model = request.GET.get("model", "")
    datas = datas.filter(model=model)

    status = request.GET.get("status", "All")
    if status and not status == 'All':
        datas = datas.filter(status=status)

    search = request.GET.get("search", "")
    if search:
        datas = datas.filter(
            Q(key__icontains=search) |  Q(json_data__icontains=search) 
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
            "key": search,
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


@login_validate
def json_data_detail(request, id):
    data = JSONData.objects.get(id=id)
    context = {
        "data": data,
        "title": "JSON DETIL"
    }
    return TemplateResponse(request, "backoffice/json_data/detil.html", context)


# for every model to generate json data
def generate_json_data(request):
    app = request.GET.get("app")
    model = request.GET.get("model")
    type = request.GET.get("type")
    save_to_json_data(app, model, type)
    return JsonResponse({"message": "Success"}, status=200)

@csrf_exempt
def process_data(request):
    key = request.GET.get("key", False)
    type = request.GET.get("type", False)
    model = request.GET.get("model", False)
    status = request.GET.get("status", False)

    qs = JSONData.objects.order_by('-id')
    if key:
        qs = qs.filter(key=key)
    if type:
        qs = qs.filter(type=type)
    if model:
        qs = qs.filter(model=model)
    if status:
        qs = qs.filter(status=status)
    if not key:
        last_key = LastKey.objects.first()
        key = last_key.last_key
        qs = qs.exclude(key=key)
    qs = qs.first()
    print(qs)

    if qs:
        LastKey.objects.all().update(last_key=qs.key)
        type=model.lower()
        if type not in ['cashflow', 'jv', 'invoice']:
            type = 'purchaseinvoice'
        response = send_to_server(type, qs)
        print(response)
    else:
        response = {"status": "error", "data": {"message": "no data found"}}
    
    if response["status"] == "success":
        qs.status="success"
        qs.response=response["data"]
        qs.save()
        return JsonResponse(response, status=200)
    else: 
        if qs:
            qs.status="failed"
            qs.response=response
            qs.save()
        return JsonResponse(response, status=400)


def send_to_server(type, data):
    sett = Settings.objects.filter(name='url_save').first()
    default = f"https://finance.cakap.com/cakap_trn/api/{type.lower()}/savetrans/";
    url = f"{sett.text_value}/api/{type.lower()}/savetrans/";
    print("sssss", url)
    body = data.json_data
    body = body.replace("'", '"')
    # body = json.loads(body)
    payload = {
        "doc": body
    }
    headers = {
        'usr': 'admin',
        'token': 'AmeZqgA4ogPXKQT9EXjpyQRtqDT2ngrd',
        'content-type': 'application/x-www-form-urlencoded'
    }
    request = requests.post(url, payload, headers=headers)
    response = request.json()
    if response["status"] == 200:
        return {"status": "success", "data": response}
    else:
        return {"status": "failed", "data": response}
        

def download_file(request, filename=''):
    if filename != '':
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(BASE_DIR)
        # Define the full file path
        filepath = BASE_DIR + '/filedownloads/' + filename
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response
    else:
        # Load the template
        return render(request, 'file.html')