"""
aiopyfcm
"""

from .message import Message
from .authenticator import PyFCMAuthenticator
from .aiopyfcm import AioPyFCM
from .errors import (
    InvalidCredentialsError,
    AioPyFCMError,
    UnspecifiedError,
    InvalidArgumentError,
    UnregisteredError,
    SenderIdMismatchError,
    QuotaExceededError,
    UnavailableError,
    InternalServerError,
    ThirdPartyAuthError
)


__TITLE__ = 'aiopyfcm'
__SUMMARY__ = 'aiopyfcm is Python Asynchronous FCM Push Controller'
__URL__ = 'https://github.com/837477/aiopyfcm'
__VERSION__ = "0.2.0"
__AUTHOR__ = '837477'
__EMAIL__ = '8374770@gmail.com'
__LICENSE__ = 'MIT License'


__all__ = [
    'Message',
    'PyFCMAuthenticator',
    'AioPyFCM',
    'InvalidCredentialsError',
    'AioPyFCMError',
    'UnspecifiedError',
    'InvalidArgumentError',
    'UnregisteredError',
    'SenderIdMismatchError',
    'QuotaExceededError',
    'UnavailableError',
    'InternalServerError',
    'ThirdPartyAuthError',
    __TITLE__,
    __SUMMARY__,
    __URL__,
    __VERSION__,
    __AUTHOR__,
    __EMAIL__,
    __LICENSE__
]
