from django.http import JsonResponse
from django.template.response import TemplateResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from sapujagad.apps.banner.models import Banner
from sapujagad.apps.blog.models import Blog
from sapujagad.apps.menu.models import Menu
from sapujagad.apps.portfolio.models import Portfolio
from sapujagad.apps.pricing.models import Pricing
from sapujagad.apps.service.models import Service
from sapujagad.apps.settings.models import Settings
from sapujagad.apps.team.models import Team
from sapujagad.apps.testimoni.models import Testimoni
from sapujagad.core.serializer import serialize_settings

from .forms import ContactusForm


def index(request):
    settings = Settings.objects.all()
    serialize_settings_dict={}
    for setting in settings:
        serialize_settings_dict[setting.name] = serialize_settings(setting)    
    form = ContactusForm(data=request.POST or None)
    menus = Menu.objects.filter(is_active=True).order_by('order')
    context = {
        "banners" : Banner.objects.filter(is_active=True).order_by('-id'),
        "blogs" : Blog.objects.filter(is_active=True).order_by('-id')[:3],
        "menus" : menus,
        "menu_list" : [menu.one_page_url for menu in menus],
        "portfolios" : Portfolio.objects.filter(is_active=True).order_by('id'),
        "pricings" : Pricing.objects.filter(is_active=True).order_by('-id'),
        "services" : Service.objects.filter(is_active=True).order_by('-id'),
        "teams" : Team.objects.filter(is_active=True).order_by('-id'),
        "testimonies" : Testimoni.objects.filter(is_active=True).order_by('id'),
        "settings" : serialize_settings_dict,
        "form": form,
        "homepage": True
    }
    return TemplateResponse(request, 'frontend/index.html', context)

def contactus(request):
    form = ContactusForm(data=request.POST or None)
    if form.is_valid():
        form.save()
    data={"success": "true", "message":""}
    return JsonResponse(data)


def blogdetail(request, slug):
    settings = Settings.objects.all()
    serialize_settings_dict={}
    for setting in settings:
        serialize_settings_dict[setting.name] = serialize_settings(setting)

    blog = Blog.objects.get(slug=slug)
    blogs = Blog.objects.filter(is_active=True)\
        .exclude(slug=slug).order_by('-id')[:3]
    menus = Menu.objects.filter(is_active=True).order_by('order')
    return TemplateResponse(request, 'frontend/blog-detail.html', {
        "blog": blog, 
        "blogs": blogs, 
        "menus" : menus,
        "menu_list" : [menu.one_page_url for menu in menus],
        "settings" : serialize_settings_dict,
        "homepage": False
    })


def lazy_load_blogs(request):
    page = request.POST.get('page')
    blogs = Blog.objects.filter(is_active=True).all().order_by('-id')
    results_per_page = 3
    paginator = Paginator(blogs, results_per_page)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(2)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    # build a html blogs list with the paginated blogs
    blogs_html = loader.render_to_string(
        'frontend/blogs.html',
        {'blogs': blogs}
    )
    output_data = {
        'blogs_html': blogs_html,
        'has_next': blogs.has_next()
    }
    return JsonResponse(output_data)
