"""
This module contains the ErrorCode for aiopyfcm.
https://firebase.google.com/docs/reference/fcm/rest/v1/ErrorCode
"""


class InvalidCredentialsError(Exception):
    """
    Raised when the credentials provided are invalid.
    """
    pass


class AioPyFCMError(Exception):
    """
    Raised when an error occurs in AioPyFCM.
    """
    pass


class UnspecifiedError(AioPyFCMError):
    """
    No more information is available about this error.
    """
    pass


class InvalidArgumentError(AioPyFCMError):
    """
    Request parameters were invalid.
    An extension of type google.rpc.BadRequest is returned to specify which field was invalid.
    """
    pass


class UnregisteredError(AioPyFCMError):
    """
    App instance was unregistered from FCM.
    This usually means that the token used is no longer valid and a new one must be used.
    """
    pass


class SenderIdMismatchError(AioPyFCMError):
    """
    The authenticated sender ID is different from the sender ID for the registration token.
    """
    pass


class QuotaExceededError(AioPyFCMError):
    """
    Sending limit exceeded for the message target.
    An extension of type google.rpc.QuotaFailure is returned to specify which quota was exceeded.
    """
    pass


class UnavailableError(AioPyFCMError):
    """The server is overloaded."""
    pass


class InternalServerError(AioPyFCMError):
    """An unknown internal error occurred."""
    pass


class ThirdPartyAuthError(AioPyFCMError):
    """APNs certificate or web push auth key was invalid or missing."""
    pass
