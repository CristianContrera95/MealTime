from django.urls import path, include

from .utils.healthz import healthz


urlpatterns = [
    path("healthz", healthz, name="healthz"),
    path("menu", include('meal_delivery.urls'))
]
