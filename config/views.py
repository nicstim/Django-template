from .models import *


def get_upload_to(instance, filename) -> str:
    """
      Returns the path to the media
    """
    return 'upload/%d/%s' % (instance.id, filename)


def common_context() -> dict:
    """
      Returns the context that is present on all pages
    """
    context = dict()
    context['cfg'] = Config.get_cfg()
    return context
