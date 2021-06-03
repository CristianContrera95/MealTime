from rest_framework.exceptions import APIException
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_409_CONFLICT,
    HTTP_404_NOT_FOUND
)


class APINotMenuException(APIException):
    status_code: int = HTTP_404_NOT_FOUND
    default_detail: str = 'Menu not found.'
    default_code: str = 'error'

    def __init__(self, detail: str = None, code: str = None) -> None:
        super().__init__(detail=detail, code=code)


class APIValidationException(APIException):
    status_code: int = HTTP_400_BAD_REQUEST
    default_detail: str = 'Invalid input.'
    default_code: str = 'invalid'

    def __init__(self, detail: str = None, code: str = None) -> None:
        super().__init__(detail=detail, code=code)


class APIConflictException(APIException):
    status_code: int = HTTP_409_CONFLICT
    default_detail: str = 'Conflict with any resource.'
    default_code: str = 'conflict'

    def __init__(self, detail: str = None, code: str = None) -> None:
        super().__init__(detail=detail, code=code)


class APIMessageException(APIException):
    status_code: int = HTTP_400_BAD_REQUEST
    default_detail: str = 'Invalid request.'
    default_code: str = 'invalid'

    def __init__(self, status_code: int, detail: str = None, code: str = None) -> None:
        if not detail:
            detail = 'It seems that an error occurred while entering the data. ' \
                     'Please check again that everything is correct.'
        self.status_code = status_code
        super().__init__(detail=detail, code=code)
