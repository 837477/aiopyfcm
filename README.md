<br><br><br>
<p align="center">
  <a href="https://github.com/837477/aiopyfcm"><img src="https://github.com/user-attachments/assets/5825c842-8031-4ada-ab37-e2be74653e69"></a>
</p>
<p align="center">
    <em>From now on, you will be able to conveniently send FCM messages asynchronously through Python.</em>
</p>
<p align="center">
<a href="https://github.com/837477/aiopyfcm/blob/main/LICENSE" target="_blank">
    <img src="https://img.shields.io/pypi/l/aiopyfcm?color=FEC301" alt="License">
</a>
<a href="https://pypi.org/project/aiopyfcm" target="_blank">
    <img src="https://img.shields.io/pypi/v/aiopyfcm?color=FEC301" alt="Package version">
</a>
<a href="https://pypi.org/project/aiopyfcm" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/aiopyfcm?color=FEC301" alt="Supported Python versions">
</a>
</p>
<br><br><br>

---

**Github**: <a href="https://github.com/837477/aiopyfcm" target="_blank">https://github.com/837477/aiopyfcm </a><br>
**PyPi**: <a href="https://pypi.org/project/aiopyfcm" target="_blank">https://pypi.org/project/aiopyfcm </a>

---

You can now easily send asynchronous FCM messages!<br>
`aiopyfcm` offers the following features:

- Support for sending FCM messages with Python's Asyncio
- Compatibility with all types of messages supported by FCM
- A user-friendly message sending interface
- Simple handling of Firebase credentials (Json File / Json String / Dict)
- Automatic access token refresh
- Enhanced performance efficiency by maintaining asynchronous sessions based on your needs
- Comprehensive control over all exception scenarios in FCM

## Requirements

If you're planning to use FCM, you’ve probably already looked into it.<br>
As you may know, `google_application_credentials` is required to use FCM.<br>
**Please note that the existing Cloud Messaging API server key will be deprecated on June 20, 2024. It's advisable to obtain a `google_application_credentials` key moving forward.**

To authenticate a service account and allow it access to Firebase services, you'll need to generate a private key file in JSON format.

To generate a private key file for your service account: <br>
1. In the Firebase console, open Settings: <a href="https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk?_gl=1*pput8o*_up*MQ..*_ga*MTQ0NTkyMjIzOC4xNzExMTMyOTM2*_ga_CW55HF8NVT*MTcxMTEzMjkzNi4xLjAuMTcxMTEzMjkzNi4wLjAuMA.." target="_blank">Service Accounts. </a>
2. Click Generate New Private Key, then confirm by clicking Generate Key.
3. Securely store the JSON file containing the key.

For a more detailed explanation, please refer to the following official document.<br>
https://firebase.google.com/docs/cloud-messaging/migrate-v1#provide-credentials-using-adc


## Installation

```console
$ pip install aiopyfcm
```

## Example

You can use it flexibly according to your development situation. (Check it in the `example.py` file)

### Authenticate Google Credentials
This sample shows how to authenticate with Google credentials.

```Python
import json
import aiopyfcm


def sample_authenticate():
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
```

### Refresh Access Token
This sample shows how to refresh the Google Access Token.

```Python
def sample_refresh_access_token():
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
```

### Send Message
This sample is used when you want to maintain an asynchronous session of aiohttp.<br>
You can use resources efficiently by not opening a session every time you send.

```Python
import asyncio
import aiopyfcm

async def send_stateful():
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
```

## Contributing
The following is a set of guidelines for contributing to `aiopyfcm`. These are mostly guidelines, not rules.<br>
Use your best judgment, and feel free to propose changes to this document in a pull request.

1. Please create a branch in this format, **`<Issue Number>-<Some name>`**
2. Open a terminal and navigate to your project path. And enter this.
   **`git config --global commit.template .gitmessage.txt`**
3. You can use the template, with `git commit` through vi. **Not** `git commit -m`
4. If you want to merge your work, please pull request to the `develop` branch.
5. Enjoy contributing!

If you have any other opinions, please feel free to suggest 😀

## License

This project is licensed under the terms of the MIT license.
