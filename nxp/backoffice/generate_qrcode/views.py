import string
import random
import csv
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.template.response import TemplateResponse
from django.http import JsonResponse

from nxp.apps.serial_number.models import SerialNumber
from nxp.apps.user.decorators import login_validate

from django.http import HttpResponse
from sequences import get_next_value
from django.db import transaction



@login_validate
def index(request):
    serials = SerialNumber.objects.all().order_by('-order')
    page = request.GET.get("page")
    search = request.GET.get("search", "")
    start = request.GET.get("start", 0)
    end = request.GET.get("end", 0)

    if start and end:
        _filter = list(range(int(start), int(end)+1))
        serials = serials.filter(order__in=_filter)
    

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

    context = {
        "serials": serials,
        "title": "Serial Number",
        "filter": {"search": search, "status": status, "type": type, "start": start, "end": end},
        "new_count": new_count,
        "redeem_count": redeem_count,
    }

    return TemplateResponse(request, "backoffice/serial/index.html", context)


def generate_serial(num):
    serials = []
    serials_str = []
    rp1000 = [1000] * int (0.03 * num)
    rp500 = [500] * int (0.04 * num)
    rp400 = [400] * int (0.93 * num)
    list_value = rp1000 + rp500 + rp400

    for _ in range(num):
        duplicate = True
        while duplicate:
            code = "".join([random.choice(string.ascii_uppercase + string.digits) for i in range(
                10)])
            exists = code in serials_str
            serial = SerialNumber.objects.filter(serial_number=code).first()
            if not serial and not exists:
                serials_str.append(code)
                duplicate = False
        serial = SerialNumber(
            serial_number=code, order=get_next_value("order"), value=list_value.pop())
        serials.append(serial)
    SerialNumber.objects.bulk_create(serials)


def generate(request):
    amount = request.POST.get('amount', 0)
    if not int(amount) % 100 == 0:
        return JsonResponse({"status": "Jumlah harus kelipatan 100"}, safe=False, status=400)
    _type = request.POST.get('type')
    with transaction.atomic():
        generate_serial(int(amount))
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
