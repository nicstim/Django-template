from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models import User
from django.utils.crypto import get_random_string


class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name=_("Пользователь"), blank=True, on_delete=models.SET_NULL, null=True)
    session = models.CharField(_("Сессия"), max_length=130)

    class Meta:
        verbose_name = _("Корзина")
        verbose_name_plural = _("Корзины")

    def __str__(self):
        return _(f"Корзина #{self.id}")

    @classmethod
    def get_cart(cls, session=None, user=None):
        """
          Метод получения корзины на основе  уникального ключа.
        """
        cart_instance = None

        if session:
            cart_instance = cls.objects.filter(session=session).first()

        if user:
            cart_instance = cls.objects.filter(user=user).first()

        if not cart_instance:
            if not session:
                session = get_random_string(length=32).upper()
            cart_instance = cls.objects.create(session=session, user=user)

        return cart_instance

    @classmethod
    def cart_by_request(cls, request):
        """
          Получение корзины из request
        """
        user = None
        session_key = request.COOKIES.get(settings.SESSION_COOKIE_NAME, None)
        if not session_key and not request.session.exists(request.session.session_key):
            request.session.create()
            session_key = request.session.session_key
        if request.user.is_authenticated:
            user = request.user
        cart = cls.get_cart(session=session_key, user=user)

        return cart


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, verbose_name=_("Корзина"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Товар в корзине")
        verbose_name_plural = _("Товары в корзине")

    def __str__(self):
        return _(f"Товар #{self.id}")
