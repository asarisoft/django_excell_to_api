from django.http import JsonResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.template.response import TemplateResponse
from nxp.apps.user.models import User
from nxp.apps.reward.models import Scan
from nxp.apps.user.decorators import login_validate
from django.shortcuts import get_object_or_404
from django.utils import timezone


@login_validate
def users(request):
    users = User.objects.all().order_by("-id").exclude(is_superuser=True)
    page = request.GET.get("page")
    search = request.GET.get("search", "")
    if search:
        users = users.filter(
            Q(name__icontains=search) | Q(mobile_number__icontains=search) |
            Q(dealer_name__icontains=search)
        )

    results_per_page = 30
    paginator = Paginator(users, results_per_page)
    try:
        users = paginator.get_page(page)
    except PageNotAnInteger:
        users = paginator.get_page(1)
    except EmptyPage:
        users = paginator.get_page(paginator.num_pages)

    context = {
        "users": users,
        "title": "User",
        "filter": {"search": search},
    }
    return TemplateResponse(request, "backoffice/users/index.html", context)

@login_validate
def user_detail(request, id):
    user = User.objects.get(id=id)
    scans = Scan.objects.filter(user=user).order_by('-datetime').select_related('serial_number')
    context = {
        "user": user,
        "title": "User Detail",
        "scans": scans[0:8]
    }
    return TemplateResponse(request, "backoffice/users/user-detail.html", context)
