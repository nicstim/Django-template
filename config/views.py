from .models import *


def common_context() -> dict:
    """
      Возвращает context, который присутствует на всех страницах
    """
    context = dict()
    context['cfg'] = Config.get_cfg()
    return context
