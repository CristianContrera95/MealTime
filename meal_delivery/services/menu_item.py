from uuid import UUID
from typing import Dict, List

from meal_delivery.serializers.menu_item import MenuItemSerializer
from meal_delivery.models.menu_item import MenuItem
from meal_delivery.managers import MenuItemManager
from meal_delivery.exceptions import (
    APIValidationException,
    APIMessageException
)


class MenuItemService:
    __data: Dict
    __menu_items: List[MenuItem] = []
    __menu_item_manager: MenuItemManager

    def __init__(self):
        self.__menu_item_manager = MenuItem.objects

    def __validate_options(self) -> None:
        for item in self.__data.get('items'):
            if not isinstance(item['option_num'], int):
                raise APIValidationException(detail=f'param "option_num" in items is not integer')

    def __validate_menu_exists(self) -> None:
        pass

    def __fmt_items_dict(self) -> None:
        for item in self.__data.get('items'):
            item.update({'menu': self.__data.get('menu')})

    def __validate_items(self) -> None:
        serializer = MenuItemSerializer(
            data=self.__data,
            partial=True
        )
        if not serializer.is_valid():
            raise APIMessageException(status_code=400)

    def create_items(self, items: List[Dict], menu) -> List[MenuItem]:
        self.__data = {'items': items, 'menu': menu}
        self.__validate_items()
        self.__validate_menu_exists()
        self.__validate_options()
        self.__fmt_items_dict()

        for item in self.__data.get('items'):
            self.__menu_items.append(MenuItem(**item))

        self.__menu_item_manager.bulk_create(self.__menu_items)
        return self.__menu_items

    def get_items_by_menu(self, menu_id: UUID):
        return self.__menu_item_manager.load_all_by_menu_id(menu_id)
