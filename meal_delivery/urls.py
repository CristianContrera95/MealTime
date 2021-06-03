from django.urls import path, include

from meal_delivery.views import (
    new_menu,
    get_menu,
    order_menu,
    new_menu_api,
    index
)


app_name = "meal_delivery"


meal_api_urs = [
    path('/new', new_menu_api, name="new"),
    path('/get/<uuid:menu_uuid>', get_menu, name="get"),
    path('/<uuid:menu_uuid>', order_menu, name="order"),
]


meal_urls = [
    path('', index, name="index"),
    path('/new', new_menu, name="create")
]


urlpatterns = [
    path("/api", include(meal_api_urs)),
    path("", include(meal_urls))
]