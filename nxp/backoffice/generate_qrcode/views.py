import string
import random
import csv
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.template.response import TemplateResponse
from django.http import JsonResponse

from nxp.apps.serial_number.models import SerialNumber
from nxp.apps.user.decorators import login_validate

from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics import renderPDF
from sequences import get_next_value
from django.db import transaction



@login_validate
def index(request):
    serials = SerialNumber.objects.all().order_by('-order')
    page = request.GET.get("page")
    search = request.GET.get("search", "")
    if search:
        serials = serials.filter(serial_number=search)

    status = request.GET.get("status")
    if status:
        serials = serials.filter(status=status)

    type = request.GET.get("type")
    if type:
        serials = serials.filter(type=type)

    action = request.GET.get("action")
    if action == 'export':
        response = HttpResponse(
            content_type='text/csv',
            # headers={'Content-Disposition': 'attachment; filename="qrcode.csv"'},
        )
        writer = csv.writer(response)
        writer.writerow(['No', 'Qr-Code', 'Status'])
        idx = 0
        for sr in serials:
            idx += 1
            writer.writerow([idx, sr.serial_number, sr.status])
        return response

    results_per_page = 60
    new_count = serials.filter(status="new").count()
    redeem_count = serials.filter(status="redeem").count()

    paginator = Paginator(serials, results_per_page)
    try:
        serials = paginator.get_page(page)
    except PageNotAnInteger:
        serials = paginator.get_page(1)
    except EmptyPage:
        serials = paginator.get_page(paginator.num_pages)

    last = SerialNumber.objects.order_by('-id').first()

    context = {
        "serials": serials,
        "title": "Serial Number",
        "filter": {"search": search, "status": status, "type": type},
        "new_count": new_count,
        "redeem_count": redeem_count,
    }

    return TemplateResponse(request, "backoffice/serial/index.html", context)


def generate_serial(prefix, num, counter):
    serials = []
    serials_str = []
    for _ in range(num):
        duplicate = True
        while duplicate:
            code = "".join([random.choice(string.ascii_uppercase) for i in range(
                4)])+"-"+"".join([random.choice(string.digits) for i in range(5)])
            exists = code in serials_str
            serial = SerialNumber.objects.filter(serial_number=code).first()
            if not serial and not exists:
                serials_str.append(code)
                duplicate = False

        code = f"{prefix}-"+code
        serial = SerialNumber(
            serial_number=code, type=prefix, order=get_next_value("order"))
        serials.append(serial)
        print(serials)
    SerialNumber.objects.bulk_create(serials)


def generate(request):
    urutan = request.POST.get('urutan')
    amount = request.POST.get('amount', 0)
    _type = request.POST.get('type')
    with transaction.atomic():
        generate_serial(_type, int(amount), urutan)
    return JsonResponse({"status": "OK"}, safe=False)


def print_barcode(request):
    start = request.GET.get("start", 0)
    end = request.GET.get("end", 0)
    _filter = list(range(int(start), int(end)+1))
    serials = SerialNumber.objects.filter(order__in=_filter).order_by('-order')

    context = {
        "serials": serials,
        "title": "Print Number",
    }
    return TemplateResponse(request, "backoffice/serial/print.html", context)
