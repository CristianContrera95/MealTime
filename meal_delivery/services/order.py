from copy import copy
from uuid import UUID
from typing import Dict

from django.core.exceptions import ValidationError

from meal_delivery.models.order import Order
from meal_delivery.models.menu_item import MenuItem
from meal_delivery.serializers.order import OrderSerializer
from meal_delivery.managers import OrderManager
from meal_delivery.exceptions import (
    APIValidationException,
    APIMessageException
)


class OrderService:
    # __user: User
    __data: Dict
    __order: Order
    __order_manager: OrderManager

    def __init__(self):
        # self.__user = user if isinstance(user, User) else None
        self.__order_manager = Order.objects

    def __validate_order(self) -> None:
        serializer = OrderSerializer(
            data=self.__data,
            partial=True
        )
        if not serializer.is_valid():
            raise APIMessageException(status_code=400)

    def __validate_menu_item(self) -> None:
        menu_item_id = self.__data.get('menu_item')
        menu_item = MenuItem.objects.load_by_id(menu_item_id)
        if menu_item is None:
            raise APIValidationException(detail=f'value of "menu_item" not found')

        self.__data['menu_item'] = menu_item

    def create_order_from_view(self, data: Dict) -> Dict:
        self.__data = copy(data)

        try:
            self.__validate_order()
            self.__validate_menu_item()

            self.__order = Order(**{'customizations': self.__data['customizations'],
                                    'menu_item': self.__data['menu_item']})
            self.__order.full_clean()
            self.__order.save()

        except ValidationError as exception:
            raise APIValidationException(detail=exception.messages[0]) from exception
        except RuntimeError as exception:
            raise APIMessageException(status_code=400) from exception

        return {
            'id': self.__order.id
        }

    def get_order_by_id(self, order_id: UUID):
        return self.__order_manager.load_by_id(order_id)
