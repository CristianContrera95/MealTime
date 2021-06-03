from django.db.models import CharField, ForeignKey, CASCADE
from django.utils.translation import gettext_lazy as _

from meal_delivery.managers import OrderManager
from .common import CommonModel, ErrorMessages
from .menu_item import MenuItem


class Order(CommonModel):
    model_name = 'Order'

    menu_item: MenuItem = ForeignKey(
        verbose_name=_('Menu Item'),
        to=MenuItem,
        on_delete=CASCADE,
        null=False,
        blank=False,
        error_messages=ErrorMessages.get_field(model=model_name, field='menu_item')
    )
    customizations: str = CharField(
        verbose_name=_("Specify customizations"),
        max_length=255,
        null=True,
        blank=True,
        error_messages=ErrorMessages.get_char_field(model=model_name,
                                                    max_length=255,
                                                    field="customizations")
    )

    objects: OrderManager = OrderManager()

    class Meta(CommonModel.Meta):
        db_table = 'order'
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self) -> str:
        return f'Option {self.menu_item}'
