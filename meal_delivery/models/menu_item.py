from datetime import date
from typing import List, Dict

from django.db.models import (
    CharField,
    ForeignKey,
    CASCADE,
    IntegerField
)
from django.utils.translation import gettext_lazy as _

from meal_delivery.managers import MenuItemManager
from .common import CommonModel, ErrorMessages
from .menu import Menu


class MenuItem(CommonModel):
    model_name = 'MenuItem'

    option_num: int = IntegerField(
        verbose_name=_('Option number'),
        null=False,
        blank=False,
        error_messages=ErrorMessages.get_field(model=model_name, field='option_num'),
    )
    description: str = CharField(
        verbose_name=_('Description'),
        max_length=255,
        error_messages=ErrorMessages.get_char_field(model=model_name, field='description')
    )
    menu: Menu = ForeignKey(
        verbose_name=_('Menu'),
        to=Menu,
        on_delete=CASCADE,
        null=False,
        blank=False,
        error_messages=ErrorMessages.get_field(model=model_name, field='items')
    )

    objects: MenuItemManager = MenuItemManager()

    class Meta(CommonModel.Meta):
        db_table = 'menu_item'
        verbose_name = _('Menu Item')
        verbose_name_plural = _('Menus Items')
        ordering = ('option_num',)
        unique_together = ('menu', 'option_num')

    def __str__(self) -> str:
        # Option 1: Corn pie, Salad and Dessert
        return f'Option {self.option_num}: {self.description}'  # pylint: disable=no-member
