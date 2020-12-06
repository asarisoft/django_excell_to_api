from django.template.response import TemplateResponse
from nxp.apps.formulir.models import Formulir
from .forms import ContactusForm


def index(request):
    form = ContactusForm(data=request.POST or None)
    context = {
        "form": form,
    }
    return TemplateResponse(request, 'frontend/index.html', context)
