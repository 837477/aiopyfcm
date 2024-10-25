import time
import json
import google.auth.transport.requests
from google.oauth2 import service_account
from typing import Union, Iterable
from .errors import InvalidCredentialsError


class PyFCMAuthenticator:
    def __init__(self):
        """PyFCMAuth Initialization"""
        self.scopes: Iterable[str] = ('https://www.googleapis.com/auth/firebase.messaging',)
        self.latest_refresh_time = 0
        self.auto_refresh = None
        self._credentials = None

    @property
    def project_id(self):
        """Get project id from credentials"""
        if not self._credentials:
            raise InvalidCredentialsError("credentials_initialization_required")
        return self._credentials.project_id

    @property
    def access_token(self):
        """Get access token from credentials"""
        if not self._credentials:
            raise InvalidCredentialsError("credentials_initialization_required")
        if self.auto_refresh:
            self.refresh_credentials()
        return self._credentials.token

    def update_auto_refresh(self, auto_refresh: bool):
        """Update auto refresh setting"""
        self.auto_refresh = auto_refresh

    def refresh_credentials(self):
        """Refresh credentials"""
        now_time = time.time()
        if now_time - self.latest_refresh_time > 1800:
            request = google.auth.transport.requests.Request()
            self._credentials.refresh(request)
            self.latest_refresh_time = now_time

    def init_credentials_from_file(
        self,
        credentials_file_path: str,
        auto_refresh: bool = True
    ):
        """
        Initialize credentials from file

        :param credentials_file_path: Path to the json file containing the credentials.
        :param auto_refresh: Decide whether to automatically refresh the Google Access Token.
          - True (Default): The Access Token is checked immediately before sending the message,
                            and is automatically renewed 30 minutes before expiration.
          - False: Access Token is not refreshed automatically. (Suitable for short-term use.)
        """
        self._credentials = service_account.Credentials.from_service_account_file(
            filename=credentials_file_path,
            scopes=self.scopes
        )
        self.auto_refresh = auto_refresh
        self.refresh_credentials()

    def init_credentials(
        self,
        credentials: Union[str, dict],
        auto_refresh: bool = True
    ):
        """
        Initialize credentials from json string or dict

        :param credentials: Json string or dictionary containing the credentials.
        :param auto_refresh: Decide whether to automatically refresh the Google Access Token.
          - True (Default): The Access Token is checked immediately before sending the message,
                            and is automatically renewed 30 minutes before expiration.
          - False: Access Token is not refreshed automatically. (Suitable for short-term use.)
        """
        self._credentials = service_account.Credentials.from_service_account_info(
            info=(
                credentials
                if isinstance(credentials, dict)
                else json.loads(credentials)
            ),
            scopes=self.scopes
        )
        self.auto_refresh = auto_refresh
        self.refresh_credentials()
