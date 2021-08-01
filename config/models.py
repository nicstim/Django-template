from django.db import models


class Config(models.Model):
    title = models.CharField("Наименование", max_length=130)
    description = models.TextField("Описание")
    key = models.CharField("Ключ", max_length=130)
    value = models.TextField("Значение")

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Найстройки"

    def __str__(self):
        return self.title

    @classmethod
    def get_cfg(cls):
        context = {}
        for cfg in cls.objects.all():
            context[cfg.key] = cfg.value

        return context
