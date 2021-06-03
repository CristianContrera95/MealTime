from rest_framework.serializers import SerializerMethodField

from meal_delivery.models.menu import Menu
from meal_delivery.models.menu_item import MenuItem
from .common import DynamicFieldsSerializer
from .menu_item import MenuItemSerializer


class MenuSerializer(DynamicFieldsSerializer):
    items = SerializerMethodField()

    class Meta:
        model = Menu
        fields = ('id', 'for_day', 'items')

    def get_items(self, obj: Menu):  # pylint: disable=no-self-use
        items_response = []

        items = MenuItem.objects.load_all_by_menu_id(menu_id=obj.id)
        for item in items:
            new_item = MenuItemSerializer(instance=item, many=False).data
            items_response.append(new_item)
        return items_response
