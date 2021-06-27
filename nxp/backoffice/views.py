from django.apps.registry import apps
from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from nxp.apps.reward.models import Redeem
from nxp.apps.user.decorators import login_validate
from nxp.backoffice.forms import LoginForm

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
    redeems = Redeem.objects.all()
    context = dict(
        new_count=redeems.filter(status="new").count(),
        paid_count=redeems.filter(status="paid").count(),
        cancelled_count=redeems.filter(status="cancelled").count(),
        ovo_count=redeems.filter(wallet_type="ovo").count(),
        gopay_count=redeems.filter(wallet_type="gopay").count(),
        dana_count=redeems.filter(wallet_type="dana").count(),
        shopee_pay_count=redeems.filter(wallet_type="shopee_pay").count(),
    )
    return TemplateResponse(request, "backoffice/index.html", context)
