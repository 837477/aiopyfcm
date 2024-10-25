import json
import asyncio
import aiopyfcm


def sample_authenticate():
    """
    This sample shows how to authenticate with Google credentials.
    """

    # Initialize the PyFCMAuthenticator object.
    authenticator = aiopyfcm.PyFCMAuthenticator()

    # If you want to authenticate with your Google credentials file path, use the following method.
    authenticator.init_credentials_from_file(
        credentials_file_path="<your_credentials_path>/credentials.json",
        auto_refresh=True  # Default is True
    )

    # If you want to Google credentials in a dictionary format, use the following method.
    credentials_dict = {
        "type": "service_account",
        "project_id": "<PROJECT_ID>",
        "private_key_id": "<PRIVATE_KEY_ID>",
        "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
        "client_email": "<SERVICE_ACCOUNT_EMAIL>",
        "client_id": "<CLIENT_ID>",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "<auth_provider_x509_cert_url>",
        "client_x509_cert_url": "<client_x509_cert_url>",
        "universe_domain": "googleapis.com"
    }
    authenticator.init_credentials(
        credentials=credentials_dict,
        auto_refresh=True  # Default is True
    )

    # If you want to Google credentials as a JSON string, use the following method.
    credentials_dumps = json.dumps(credentials_dict)
    authenticator.init_credentials(
        credentials=credentials_dumps,
        auto_refresh=True  # Default is True
    )

    return authenticator


def sample_refresh_access_token():
    """
    This sample shows how to refresh the Google Access Token.
    """

    # If you set the auto_refresh value to False during the init_credentials process,
    # you will need to manually refresh the access_token.
    authenticator = sample_authenticate()
    authenticator.update_auto_refresh(False)

    # [Refresh the access token]
    # The validity period of a Google AccessToken is approximately 1 hour,
    # so you need to manually refresh it before it expires.
    authenticator.refresh_credentials()

    # If you set the auto_refresh flag to True,
    # the PyFCMAuthenticator will automatically refresh your access_token every 30 minutes.
    authenticator.update_auto_refresh(True)


async def send_stateful():
    """
    This sample is used when you want to maintain an asynchronous session of aiohttp.
    You can use resources efficiently by not opening a session every time you send.
    """

    # Get the PyFCMAuthenticator object.
    authenticator = sample_authenticate()

    # Initialize the AioPyFCM object.
    async_pyfcm = aiopyfcm.AioPyFCM(authenticator)

    # Create a message object.
    message = {
        "token": "<FCM_TOKEN>",
        "notification": {
            "title": "Sample Title",
            "body": "Sample Body",
            "image": "https://example.com/sample.jpg"
        }
    }

    # Send the message. (Stateful - Recommended)
    async with async_pyfcm as pyfcm:
        responses = await asyncio.gather(
            pyfcm.send(message),
            pyfcm.send(message),
            pyfcm.send(message),
        )
        print(responses)


async def send_stateless():
    """
    This sample does not maintain the aiohttp asynchronous session,
    so it connects the session every time you send.
    """

    # Get the PyFCMAuthenticator object.
    authenticator = sample_authenticate()

    # Initialize the AioPyFCM object.
    async_pyfcm = aiopyfcm.AioPyFCM(authenticator)

    # Create a message object.
    message = {
        "token": "<FCM_TOKEN>",
        "notification": {
            "title": "Sample Title",
            "body": "Sample Body",
            "image": "https://example.com/sample.jpg"
        }
    }

    # Send the message. (Stateless)
    responses = await asyncio.gather(
        async_pyfcm.send(message),
        async_pyfcm.send(message),
        async_pyfcm.send(message),
    )
    print(responses)
