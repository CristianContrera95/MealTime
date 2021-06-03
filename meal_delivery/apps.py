from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MealDeliveryConfig(AppConfig):
    name = 'meal_delivery'
    verbose_name = _('Meal Delivery')
