from django.conf import settings
from slugify import slugify
from django.utils import timezone


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
