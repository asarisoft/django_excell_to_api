from django.template.response import TemplateResponse
from nxp.apps.formulir.models import Formulir
from .forms import FormulirForm
from django.http import JsonResponse


def index(request):
    form = FormulirForm(data=request.POST or None)
    context = {
        "form": form,
    }
    return TemplateResponse(request, 'frontend/index.html', context)


def post_formulir(request):
    if request.is_ajax and request.method == "POST":
        form = FormulirForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "sukses"}, status=200)
        else:
            return JsonResponse({"error": "form.errors.responseText"}, status=400)
    return JsonResponse({"error": "error gk jelas hehe"}, status=400)