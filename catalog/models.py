from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

from config.views import get_upload_to


class Category(models.Model):
    IMAGE_PATH = "catalog/category"

    title = models.CharField(_("Название"), max_length=130)
    parent = models.ForeignKey("self", verbose_name=_("Родительская категория"), on_delete=models.SET_NULL, blank=True,
                               null=True)
    description = models.TextField(_("Описание"), blank=True)
    image = models.ImageField(_("Изображение"), upload_to=get_upload_to, blank=True)

    is_active = models.BooleanField(_("Статус активности"), default=True)

    class Meta:
        verbose_name = _("Категория")
        verbose_name_plural = _("Категории")

    def __str__(self) -> str:
        return self.title

    @property
    def product_count(self) -> int:
        return len(self.products.all())


class Product(models.Model):
    IMAGE_PATH = "catalog/product"

    category = models.ForeignKey(Category, verbose_name=_("Категория"),
                                 related_name='products', on_delete=models.SET_NULL, blank=True, null=True)
