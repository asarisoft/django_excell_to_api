# -*- coding: utf-8 -*-
# from django.contrib import messages
# from .forms import AddNewsForm
# from django.urls import reverse
# from django.shortcuts import redirect, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.template.response import TemplateResponse

from nxp.apps.formulir.models import Formulir
from nxp.apps.user.decorators import login_validate


@login_validate
def index(request):
    formulirs = Formulir.objects.all()
    page = request.GET.get("page")
    search = request.GET.get("search", "")
    if search:
        formulirs = formulirs.filter(Q(name=search) | Q(mobile_number=search))
    ewallet = request.GET.get("ewallet")
    if ewallet:
        formulirs = formulirs.filter(wallet_type=ewallet)
    status = request.GET.get("status")
    if status:
        formulirs = formulirs.filter(status=status)

    results_per_page = 30
    new_count = formulirs.filter(status="new").count()
    paid_count = formulirs.filter(status="paid").count()
    cancel_count = formulirs.filter(status="paid").count()

    paginator = Paginator(formulirs, results_per_page)
    try:
        formulirs = paginator.get_page(page)
    except PageNotAnInteger:
        formulirs = paginator.get_page(1)
    except EmptyPage:
        formulirs = paginator.get_page(paginator.num_pages)

    context = {
        "formulirs": formulirs,
        "title": "Fromulir",
        "filter": {"search": search, "status": status, "ewallet": ewallet},
        "new_count": new_count,
        "paid_count": paid_count,
        "cancel_count": cancel_count,
    }
    return TemplateResponse(request, "backoffice/formulir/index.html", context)


# @login_validate
# def add(request):
#     form = AddNewsForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#         messages.success(request, 'success')
#         return redirect(reverse('backoffice:news:index'))

#     context = dict(
#         form=form,
#         title='Add New'
#     )
#     return TemplateResponse(request, 'backoffice/news/add.html', context)


# @login_validate
# def edit(request, id):
#     news = get_object_or_404(News, id=id)
#     form = AddNewsForm(
#       request.POST or None, request.FILES or None, instance=news)
#     if form.is_valid():
#         form.save()
#         return redirect(reverse('backoffice:news:index'))

#     context = dict(
#         form=form,
#         title='Edit User'
#     )
#     return TemplateResponse(request, 'backoffice/news/add.html', context)


# @login_validate
# def delete(request, id):
#     news = get_object_or_404(News, id=id)
#     news.delete()
#     return redirect('backoffice:news:index')
