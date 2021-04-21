import string, random
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


@login_validate
def index(request):
    serials = SerialNumber.objects.all().order_by('-id')
    page = request.GET.get("page")
    search = request.GET.get("search", "")
    if search:
        serials = serials.filter(Q(name=search) | Q(mobile_number=search))
    status = request.GET.get("status")
    if status:
        serials = serials.filter(status=status)

    results_per_page = 60
    new_count = serials.filter(status="new").count()
    claimed_count = serials.filter(status="claimed").count()

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
        "filter": {"search": search, "status": status},
        "new_count": new_count,
        "claimed_count": claimed_count,
        "counter": int(last.generated_count)  + 1 if last else 1
    }
    return TemplateResponse(request, "backoffice/serial/index.html", context)


def generate_serial(prefix, num, counter):
    for _ in range(num):
        code = "".join([random.choice(string.ascii_uppercase) for i in range(4)])+"-"+"".join([random.choice(string.digits) for i in range(5)])
        code = f"{prefix}-"+code
        SerialNumber.objects.create(serial_number=code, generated_count=counter, type=prefix)

def generate(request):
    urutan = request.POST.get('urutan')
    _type = request.POST.get('type')
    generate_serial(_type, 60, urutan)
    return JsonResponse({"status": "OK"}, safe=False)


def print_barcode(request):
    serials = SerialNumber.objects.all().order_by('-id')
    counter = request.GET.get("counter", 0)
    if counter:
        serials = serials.filter(generated_count=int(counter))

    page = int(request.GET.get("page", 0))
    if page and page >= 1 and page <= 10:
        start = page * 6 - 6
        end = start + 6
        serials = serials[start:end]

    context = {
        "serials": serials,
        "title": "Print Number",
    }
    return TemplateResponse(request, "backoffice/serial/print.html", context)

