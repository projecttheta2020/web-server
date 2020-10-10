import enum

'''Define Enums here using enum.Enum Class'''


class ErrorCodes(enum.Enum):
    Success = 0
    InvalidRequestParams = 1
    DefaultError = 2


class SuccessCodes(enum.Enum):
    Default = 0


DEFAULT_ERROR_MESSAGE = "Something Went Wrong. Please Try Again Later"
DEFAULT_SUCCESS_MESSAGE = "Operation Completed Successfully"

ERROR_MESSAGES_DICT = {
    ErrorCodes.Success.value: "Success",
    ErrorCodes.InvalidRequestParams.value: "Invalid Request",
    ErrorCodes.DefaultError.value: DEFAULT_ERROR_MESSAGE,
}

SUCCESS_MESSAGES_DICT = {
    SuccessCodes.Default.value: DEFAULT_SUCCESS_MESSAGE,
}
