from rest_framework.serializers import SerializerMethodField

from meal_delivery.models.order import Order
from meal_delivery.models.menu_item import MenuItem
from .common import DynamicFieldsSerializer
from .menu_item import MenuItemSerializer


class OrderSerializer(DynamicFieldsSerializer):
    menu_item = SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'menu_item', 'customizations')

    def get_menu_item(self, obj: Order):  # pylint: disable=no-self-use
        item = MenuItem.objects.load_by_id(obj.menu_item.id)
        new_item = MenuItemSerializer(instance=item, many=False).data
        return new_item
