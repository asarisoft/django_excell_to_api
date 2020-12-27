from django.contrib import messages
# from .forms import AddNewsForm
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from django.template.response import TemplateResponse
from nxp.apps.formulir.models import Formulir
from nxp.apps.user.decorators import login_validate
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_validate
def index(request):
    formulirs = Formulir.objects.all()
    page = request.GET.get('page')
    results_per_page = 1
    paginator = Paginator(formulirs, results_per_page)
    try:
        formulirs = paginator.page(page)
    except PageNotAnInteger:
        formulirs = paginator.page(2)
    except EmptyPage:
        formulirs = paginator.page(paginator.num_pages)

    context = dict(
        formulirs=formulirs,
        title='Fromulir'
    )
    return TemplateResponse(request, 'backoffice/formulir/index.html', context)

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
#     form = AddNewsForm(request.POST or None, request.FILES or None, instance=news)
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
