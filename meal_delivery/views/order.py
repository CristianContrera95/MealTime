from uuid import UUID

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_202_ACCEPTED

from meal_delivery.services import OrderService


@api_view(['POST'])
def order_menu(request: Request, menu_uuid: UUID) -> Response:
    """
    request.data must be:
    { 'menu_item': UUID,
      'customizations': "Sin sal"
    }
    """
    service = OrderService()
    data = service.create_order_from_view(request.data)
    return Response(data=data, status=HTTP_202_ACCEPTED)
