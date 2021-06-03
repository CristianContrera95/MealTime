import re
from copy import copy
from uuid import UUID
from datetime import datetime
from typing import Dict, List

from django.core.exceptions import ValidationError
from django.db.transaction import atomic as atomic_transaction, on_commit

from meal_delivery.models.menu import Menu
from meal_delivery.serializers.menu import MenuSerializer
from meal_delivery.managers import MenuManager
from meal_delivery.exceptions import (
    APIValidationException,
    APIConflictException,
    APINotMenuException,
    APIMessageException
)
from meal_delivery.services.menu_item import MenuItemService
from meal_delivery.models.menu_item import MenuItem


class MenuService:
    # __user: User
    __data: Dict
    __menu: Menu
    __menu_manager: MenuManager
    __menu_items: List[MenuItem] = []
    __regexp: Dict = {
        'day': re.compile(r'\d{4}-\d{2}-\d{2}'),
    }

    def __init__(self):
        # self.__user = user if isinstance(user, User) else None
        self.__menu_manager = Menu.objects

    def __validate_for_day_fmt(self) -> None:
        day = self.__data.get('for_day', None)
        if self.__regexp['day'].fullmatch(day) is None:
            raise APIValidationException(detail=f'param "for_day" has not right format')

        self.__data['for_day'] = datetime.strptime(day, '%Y-%m-%d').date()

    def __validate_unique_for_day(self) -> None:
        day = self.__data.get('for_day', None)
        if self.__menu_manager.load_by_day(day) is not None:
            raise APIConflictException(detail=f'day={day} already has menu')

    def __validate_future_for_day(self) -> None:
        if (self.__data['for_day'] - datetime.now().date()).days < 0:
            raise APIValidationException(detail=f'menu for day must be today or before')

    def __validate_has_items(self) -> None:
        items = self.__data.get('items', [])
        if not items:
            raise APIValidationException(detail=f'not items given')

    def __validate_menu(self) -> None:
        serializer = MenuSerializer(
            data=self.__data,
            partial=True
        )
        if not serializer.is_valid():
            raise APIMessageException(status_code=400,
                                      )

    def create_menu_from_view(self, data: Dict) -> Dict:
        self.__data = copy(data)
        try:
            self.__validate_menu()
            self.__validate_for_day_fmt()
            self.__validate_future_for_day()
            self.__validate_unique_for_day()
            self.__validate_has_items()
            with atomic_transaction():
                day = self.__data.get('for_day', None)

                self.__menu = Menu(**{'for_day': day})
                self.__menu.full_clean()
                self.__menu.save()

                items = self.__data.get('items', [])
                self.__menu_items = MenuItemService().create_items(items=items,
                                                                   menu=self.__menu)
        except ValidationError as exception:
            raise APIValidationException(detail=exception.messages[0]) from exception
        except RuntimeError as exception:
            raise APIMessageException(status_code=400) from exception

        return {
            'id': self.__menu.id
        }

    def get_menu_by_id(self, menu_id: UUID):
        self.__menu = self.__menu_manager.load_by_id(menu_id)
        if self.__menu is None:
            raise APINotMenuException()
        # self.__menu_items = MenuItemService().get_items_by_menu(menu_id=menu_id)
        # return MenuResponse(menu=self.__menu, items=self.__menu_items).__dict__
        return MenuSerializer(instance=self.__menu).data
