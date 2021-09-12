import json
from django.http import JsonResponse
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ScanForm, RedeemForm
from nxp.apps.reward.models import Balance
from nxp.apps.user.models import User


def scan(request):
    form = ScanForm(data=request.POST or None)
    context = {
        "form": form,
    }
    return TemplateResponse(request, "frontend/index.html", context)


def redeem(request):
    form = ScanForm(data=request.POST or None)
    context = {
        "form": form,
    }
    return TemplateResponse(request, "frontend/redeem.html", context)

@csrf_exempt
def api_scan(request):
    if request.is_ajax and request.method == "POST":
        form = ScanForm(request.POST)
        if form.is_valid():
            scan = form.save()
            value = f'{scan.serial_number.value:,}'.replace(',','.'), 
            return JsonResponse(
                {"message": "Transaksi berhasil", "value":value}, status=200)
        else:
            return JsonResponse(form.errors, status=400)
    return JsonResponse({"error": "Need Request Post and AJAX"}, status=400)

@csrf_exempt
def get_information(request):
    if request.is_ajax and request.method == "POST":
        mobile_number = request.POST.get("mobile_number", "")
        user = User.objects.filter(mobile_number=mobile_number).first()
        if not user:
            return JsonResponse({"error": "User tidak ditemukan"}, status=400)
        balances = (Balance.objects.filter(user=user)
            .select_related('redeem').select_related('scan').order_by('-id')[0:20]
        )
        response = {
            'user': user.serialize(),
            # 'balance': [balance.serialize() for balance in balances],
        }
        return JsonResponse({"data": response}, status=200)
    return JsonResponse({"error": "User Tidak Dietmukan"}, status=400)
        
@csrf_exempt
def api_redeem(request):
    if request.is_ajax and request.method == "POST":
        form = RedeemForm(request.POST)
        if form.is_valid():
            redeem = form.save()
            mobile_number = request.POST.get("mobile_number", "")
            user = User.objects.filter(mobile_number=mobile_number).first()
            balances = (Balance.objects.filter(user=user)
                .select_related('redeem').select_related('scan').order_by('-id')[0:20]
            )
            response = {
                'user': user.serialize(),
                'balance': [balance.serialize() for balance in balances],
            }
            return JsonResponse({
                "message": "Transaksi berhasil",
                "data": response
            }, status=200)
        else:
            return JsonResponse(form.errors, status=400)
    return JsonResponse({"error": "Need Request Post and AJAX"}, status=400)

