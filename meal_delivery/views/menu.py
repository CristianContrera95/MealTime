from uuid import UUID

from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

from meal_delivery.services import MenuService
from meal_delivery.forms import MenuForm



def index(request: Request) -> Response:
    return render(request, 'index.html', context={'form': MenuForm})



def new_menu(request: Request) -> Response:
    return render(request, 'new.html', context={'form': MenuForm})


@api_view(['POST'])
def new_menu_api(request: Request) -> Response:
    """
    request.data must be:
    { 'for_day': '2021-06-21',
      'items': [
         {'option_num': 1, 'description': 'Asado'},
         {'option_num': 2, 'description': 'Pure'},
      ]
   }
    """
    service = MenuService()
    data = service.create_menu_from_view(request.data)
    return Response(data=data, status=HTTP_201_CREATED)


@api_view(['GET'])
def get_menu(request: Request, menu_uuid: UUID) -> Response:
    service = MenuService()
    data = service.get_menu_by_id(menu_uuid)
    return Response(data=data, status=HTTP_200_OK)
