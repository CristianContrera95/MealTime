from datetime import date

from django.db.models import DateField
from django.utils.translation import gettext_lazy as _

from meal_delivery.managers import MenuManager
from .common import CommonModel, ErrorMessages


class Menu(CommonModel):
    model_name = 'Menu'

    # user: User = ForeignKey(
    # )
    for_day: date = DateField(
        verbose_name=_("For day"),
        null=False,
        blank=False,
        error_messages=ErrorMessages.get_field(model=model_name, field='for_day')
    )

    objects: MenuManager = MenuManager()

    class Meta(CommonModel.Meta):
        db_table = 'menu'
        verbose_name = _('Menu')
        verbose_name_plural = _('Menus')
        ordering = ('for_day',)
        unique_together = ('for_day',)

    def __str__(self) -> str:
        # return f'Hello!\nI share with you today\'s menu :)\n' \
        #        f'{self.item}'  # pylint: disable=no-member
        return f'Menu for {self.for_day}'
