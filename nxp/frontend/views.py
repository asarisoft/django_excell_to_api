from django.template.response import TemplateResponse
from nxp.apps.formulir.models import Formulir
from .forms import FormulirForm


def index(request):
    form = FormulirForm(data=request.POST or None)
    context = {
        "form": form,
    }
    return TemplateResponse(request, 'frontend/index.html', context)
