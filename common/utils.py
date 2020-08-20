from rest_framework import status
from rest_framework.response import Response

from common.consts import ErrorCodes, SuccessCodes, ERROR_MESSAGES_DICT, SUCCESS_MESSAGES_DICT, DEFAULT_ERROR_MESSAGE, DEFAULT_SUCCESS_MESSAGE


def get_error_response(error_code=ErrorCodes.InvalidRequestParams.value,
                        error_msg=None,
                        status=status.HTTP_400_BAD_REQUEST):
    if error_msg is None:
        error_msg = ERROR_MESSAGES_DICT.get(error_code, DEFAULT_ERROR_MESSAGE)
        return Response(dict(error_code=error_code, error=error_msg), status=status)


def get_success_response(response_dict=None,
                            success_code=SuccessCodes.Default.value,
                            status=status.HTTP_200_OK):
    if response_dict is None:
        response_dict = {}
    if isinstance(response_dict, dict):
        if 'message' not in response_dict.keys():
            response_dict.update({
                'message': SUCCESS_MESSAGES_DICT.get(success_code, DEFAULT_SUCCESS_MESSAGE)
            })
    return Response(response_dict, status=status)


def resolve_response(*args, **kwargs):
    data = kwargs
    if not data:
        return Response(data, status=status.HTTP_200_OK)
    
    if data.pop("error", False):
        error_code = data.pop("error_code", None)
        if not error_code:
            error_msg = data.pop("msg", None)
            data["error"] = error_msg
            return get_error_response(ErrorCodes.DefaultError.value, error_msg=error_msg)
        return get_error_response(error_code)
    else:
        success_code = kwargs.get("success_code", SuccessCodes.Default.value)
        return get_success_response(data, success_code)