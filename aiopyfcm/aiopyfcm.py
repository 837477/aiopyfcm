import aiohttp
from .authenticator import PyFCMAuthenticator
from .message import Message
from .errors import (
    UnspecifiedError, InvalidArgumentError, UnregisteredError,
    SenderIdMismatchError, QuotaExceededError, UnavailableError,
    InternalServerError, ThirdPartyAuthError
)


class AioPyFCM:

    def __init__(
        self,
        authenticator: PyFCMAuthenticator
    ):
        """AioPyFCM Initialization"""
        self.authenticator = authenticator
        self.session = None
        self.endpoint = "https://fcm.googleapis.com"

    async def __aenter__(self):
        """Open a session when entering the context."""
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        """Close the session when exiting the context."""
        await self.session.close()

    async def send(self, message: Message):
        """
        Send message to FCM server

        :param message: The message to send.
        :return: JSON response from the FCM Server.
        """
        if not self.session:
            # stateless mode: open a new session every time
            async with aiohttp.ClientSession() as session:
                return await self._post_message(message, session)
        else:
            # stateful mode: use the existing session
            return await self._post_message(message, self.session)

    async def _post_message(
        self,
        message: Message,
        session: aiohttp.ClientSession
    ):
        """
        Internal method to post a message.

        :param message: The message to send.
        :param session: The aiohttp session to use.
        """
        async with session.post(
            url=f"{self.endpoint}/v1/projects/{self.authenticator.project_id}/messages:send",
            headers={
                "Authorization": f"Bearer {self.authenticator.access_token}",
                "Content-Type": "application/json"
            },
            json={"message": message}
        ) as response:
            result = await response.json()
            return await self._handle_response(response, result)

    @staticmethod
    async def _handle_response(
        response: aiohttp.ClientResponse,
        result: dict
    ):
        """Handle various FCM response codes."""
        if response.status == 200:
            return result
        errors = {
            400: InvalidArgumentError,
            401: ThirdPartyAuthError,
            403: SenderIdMismatchError,
            404: UnregisteredError,
            429: QuotaExceededError,
            500: InternalServerError,
            503: UnavailableError,
        }
        raise errors.get(response.status, UnspecifiedError)(result)
