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
from nxp.apps.cashflow.admin import CashflowResource

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
        users = datas.filter(
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
        result = resources.import_data(dataset, dry_run=True)  # Test the data import
        print(result.has_errors())
        if not result.has_errors():
            resources.import_data(dataset, dry_run=False)  # Actually import now

    context = {
        "datas": datas,
        "title": "Cashflow",
        "filter": {"search": search},
    }
    return TemplateResponse(request, "backoffice/cashflow/index.html", context)