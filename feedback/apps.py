from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FeedbackConfig(AppConfig):
    name = 'feedback'
    verbose_name = _("Обратная связь")
