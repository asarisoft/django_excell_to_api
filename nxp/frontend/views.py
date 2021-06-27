from django.http import JsonResponse
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ScanForm


def scan(request):
    form = ScanForm(data=request.POST or None)
    context = {
        "form": form,
    }
    return TemplateResponse(request, "frontend/index.html", context)


# def redeem(request):
#     form = RedeemForm(data=request.POST or None)
#     context = {
#         "form": form,
#     }
#     return TemplateResponse(request, "frontend/index.html", context)

@csrf_exempt
def api_scan(request):
    if request.is_ajax and request.method == "POST":
        form = ScanForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "sukses"}, status=200)
        else:
            return JsonResponse(form.errors, status=400)
    return JsonResponse({"error": "error gk jelas hehe"}, status=400)


# @csrf_exempt
# def api_redeem(request):
#     if request.is_ajax and request.method == "POST":
#         form = RedeemForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({"message": "sukses"}, status=200)
#         else:
#             return JsonResponse(form.errors, status=400)
#     return JsonResponse({"error": "error gk jelas hehe"}, status=400)

