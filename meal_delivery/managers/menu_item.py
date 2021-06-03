from typing import Optional
from uuid import UUID

from .common import CommonManager

class MenuItemManager(CommonManager):

    def load_all_by_menu_id(self, menu_id: UUID) -> Optional:
        return super().filter(menu_id=menu_id).all()

    def load_by_menu_and_option(self, menu_id: UUID, option_num: int):
        return super().filter(menu_id=menu_id, option_num=option_num).all()
