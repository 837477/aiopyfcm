import aiohttp
from typing import Union
from .pyfcm_auth import PyFCMAuthenticator
from .message import Message
from .errors import (
    UnspecifiedError, InvalidArgumentError, UnregisteredError,
    SenderIdMismatchError, QuotaExceededError, UnavailableError,
    InternalServerError, ThirdPartyAuthError
)


class AioPyFCM(PyFCMAuthenticator):

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()

    def __init__(self):
        """AioPyFCM Initialization"""
        super().__init__()
        self.session = None
        self.endpoint = "https://fcm.googleapis.com"

    async def send(self, message: Message):
        """
        Send message to FCM server

        :param message: The message to send.
        :return: JSON response from the FCM Server.
        """
        if not self.session:
            async with aiohttp.ClientSession() as session:
                self.session = session
                return await self._post_message(message)
        else:
            return await self._post_message(message)

    async def _post_message(self, message: Message):
        """
        Internal method to post a message.
        """
        async with self.session.post(
            url=f"{self.endpoint}/v1/projects/{self.project_id}/messages:send",
            headers={
                "Authorization": f"Bearer {self.access_token}",
                "Content-Type": "application/json"
            },
            json={"message": message}
        ) as response:
            result = await response.json()
            if response.status == 200:
                return result
            elif response.status == 400:
                raise InvalidArgumentError(result)
            elif response.status == 401:
                raise ThirdPartyAuthError(result)
            elif response.status == 403:
                raise SenderIdMismatchError(result)
            elif response.status == 404:
                raise UnregisteredError(result)
            elif response.status == 429:
                raise QuotaExceededError(result)
            elif response.status == 500:
                raise InternalServerError(result)
            elif response.status == 503:
                raise UnavailableError(result)
            else:
                raise UnspecifiedError(result)
