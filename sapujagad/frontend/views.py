from django.template.response import TemplateResponse

from sapujagad.apps.banner.models import Banner
from sapujagad.apps.blog.models import Blog
from sapujagad.apps.menu.models import Menu
from sapujagad.apps.portfolio.models import Portfolio
from sapujagad.apps.pricing.models import Pricing
from sapujagad.apps.service.models import Service
from sapujagad.apps.settings.models import Settings
from sapujagad.apps.team.models import Team
from sapujagad.core.serializer import serialize_settings


def index(request):
    settings = Settings.objects.all()
    for setting in settings:
        serialize_settings_dict[setting.name] = serialize_settings(setting)
    context = {
        "banners" : Banner.objects.filter(is_active=True).order_by('-id'),
        "blogs" : Blog.objects.filter(is_active=True).order_by('-id')[:6],
        "menus" : Menu.objects.filter(is_active=True).order_by('order'),
        "portfolios" : Portfolio.objects.filter(is_active=True).order_by('-id'),
        "pricings" : Pricing.objects.filter(is_active=True).order_by('-id'),
        "services" : Service.objects.filter(is_active=True).order_by('-id'),
        "teams" : Team.objects.filter(is_active=True).order_by('-id'),
    }
    return TemplateResponse(request, 'frontend/index.html', context)

