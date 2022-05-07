import os
from django.conf import settings
from slugify import slugify
from django.utils import timezone
from time import time
from django.apps import apps
from nxp.apps.jsondata.models import JSONData


class FilenameGenerator(object):
    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, instance, filename):
        today = timezone.localtime(timezone.now()).date()
        filepath = os.path.basename(filename)
        filename, extension = os.path.splitext(filepath)
        filename = slugify(filename)

        path = "/".join([
            'static_files',
            self.prefix,
            str(today.year),
            str(today.month),
            # str(today.day),
            filename + extension
        ])
        return path

try:
    from django.utils.deconstruct import deconstructible
    FilenameGenerator = deconstructible(FilenameGenerator)
except ImportError:
    pass


def custom_slugify(string):
    string = "%s-%s" % (string, str(time())[11:])
    return slugify(string)


def save_to_json_data():
    datas = generate_json_all_data()

def save_to_json_data(app_label, model_name, type):
    model = apps.get_model(app_label=app_label, model_name=model_name)
    instance = model()
    datas = model().generate_json_all_data()
    for key in datas.keys():
        data = datas[key]
        item_joined = data["item_joined"]
        data.pop("item_joined")
        print(key, model_name, type)
        obj, created = JSONData.objects.update_or_create(
            key=key,
            model=model_name,
            type=type,
            defaults={
                "item_joined": item_joined,
                "json_data": data
            }
        )


# from nxp.core.utils import save_to_json_data
# save_to_json_data('cashflow', "Cashflow")