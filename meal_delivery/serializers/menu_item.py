from .common import DynamicFieldsSerializer

from meal_delivery.models.menu_item import MenuItem


class MenuItemSerializer(DynamicFieldsSerializer):

    class Meta:
        model = MenuItem
        fields = ('id', 'option_num', 'description')

    # def get_menu_day(self, obj: MenuItem):  # pylint: disable=no-self-use
    #     return obj.menu.for_day
