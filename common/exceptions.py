from rest_framework.status import HTTP_400_BAD_REQUEST

from common.consts import ErrorCodes
from common.utils import get_error_response


class ThetaValidationError(Exception):
    error_code = ErrorCodes.DefaultError.value
    error_message = None
    status = HTTP_400_BAD_REQUEST

    def __init__(self, error_code=ErrorCodes.InvalidRequestParams.value, error_message=None, status=HTTP_400_BAD_REQUEST):
        self.error_code = error_code
        self.error_message = error_message
        self.status = status

    def get_response(self):
        return get_error_response(error_code=self.error_code, error_msg=self.error_message, status=self.status)

