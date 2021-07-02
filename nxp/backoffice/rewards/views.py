from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.template.response import TemplateResponse
from nxp.apps.reward.models import Redeem, Scan
from nxp.apps.user.decorators import login_validate


@login_validate
def redeem(request):
    redeems = Redeem.objects.all().order_by("-id")
    page = request.GET.get("page")
    search = request.GET.get("search", "")
    if search:
        redeems = redeems.filter(Q(user__name__icontains=search) | Q(user__mobile_number__icontains=search))

    ewallet = request.GET.get("ewallet")
    if ewallet:
        redeems = redeems.filter(wallet_type=ewallet)
    status = request.GET.get("status")
    if status:
        redeems = redeems.filter(status=status)

    results_per_page = 30
    new_count = redeems.filter(status="new").count()
    paid_count = redeems.filter(status="paid").count()
    cancel_count = redeems.filter(status="paid").count()

    paginator = Paginator(redeems, results_per_page)
    try:
        redeems = paginator.get_page(page)
    except PageNotAnInteger:
        redeems = paginator.get_page(1)
    except EmptyPage:
        redeems = paginator.get_page(paginator.num_pages)

    context = {
        "redeems": redeems,
        "title": "Fromulir",
        "filter": {"search": search, "status": status, "ewallet": ewallet},
        "new_count": new_count,
        "paid_count": paid_count,
        "cancel_count": cancel_count,
    }
    return TemplateResponse(request, "backoffice/rewards/index.html", context)


@login_validate
def transactions(request):
    scans = Scan.objects.all().order_by("-id")
    page = request.GET.get("page")
    search = request.GET.get("search", "")
    if search:
        scans = scans.filter(
            Q(user__name__icontains=search) | Q(user__mobile_number__icontains=search) | Q(serial_number__icontains=search))

    results_per_page = 30
    paginator = Paginator(scans, results_per_page)
    try:
        scans = paginator.get_page(page)
    except PageNotAnInteger:
        scans = paginator.get_page(1)
    except EmptyPage:
        scans = paginator.get_page(paginator.num_pages)

    context = {
        "scans": scans,
        "title": "Fromulir",
        "filter": {"search": search},
    }
    return TemplateResponse(request, "backoffice/rewards/transactions.html", context)
