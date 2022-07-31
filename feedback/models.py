from django.db import models
from django.utils.translation import gettext_lazy as _


class Feedback(models.Model):
    name = models.CharField(_("Имя"), max_length=210)
    email = models.EmailField('e-mail', max_length=210)
    text = models.TextField(_("Текст"), max_length=500)

    class Meta:
        verbose_name = _("Отзыв")
        verbose_name_plural = _("Отзывы")

    def __str__(self):
        return _("Отзыв от") + self.name
