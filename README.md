<br><br><br>
<p align="center">
  <a href="https://github.com/837477/aiopyfcm"><img src="https://github.com/user-attachments/assets/5825c842-8031-4ada-ab37-e2be74653e69"></a>
</p>
<p align="center">
    <em>From now on, easily send FCM (Firebase Cloud Messages) through "aiopyfcm"</em>
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

**Documnets**: <a href="https://github.com/837477/aiopyfcm" target="_blank">https://github.com/837477/aiopyfcm </a>

---

You can now easily send asynchronous FCM messages.<br>
`aiopyfcm` has the following features:

- Support for sending Python Asyncio FCM messages
- Supports all types of messages handled by FCM
- Very convenient message sending interface
- Easily handle Firebase credentials (Json File / Json String / Dict)
- Supports automatic access token refresh.
- Increase performance efficiency by maintaining asynchronous sessions depending on the situation.
- All exception situations in FCM can be controlled.


## Requirements

If you are planning to use FCM now, I think you have already studied FCM.<br>
As you know, `google_application_credentials` is required to use FCM.<br>
**The existing Cloud Messaging API server key will be deprecated on June 20, 2024, so it is recommended to obtain a `google_application_credentials` key in the future.**

To authenticate a service account and authorize it to access Firebase services, you must generate a private key file in JSON format.

To generate a private key file for your service account: <br>
1. In the Firebase console, open Settings > <a href="https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk?_gl=1*pput8o*_up*MQ..*_ga*MTQ0NTkyMjIzOC4xNzExMTMyOTM2*_ga_CW55HF8NVT*MTcxMTEzMjkzNi4xLjAuMTcxMTEzMjkzNi4wLjAuMA.." target="_blank">Service Accounts. </a>
2. Click Generate New Private Key, then confirm by clicking Generate Key.
3. Securely store the JSON file containing the key.

For a more detailed explanation, please refer to the following official document.<br>
https://firebase.google.com/docs/cloud-messaging/migrate-v1#provide-credentials-using-adc


## Installation

```console
$ pip install aiopyfcm
```

## Example

You can use it flexibly according to your development situation.
* You can check it in the `example.py` file.

```Python
import json
import asyncio
import aiopyfcm


async def credentials_sample_1():
    """
    This example demonstrates an authorization method using a JSON file.
    """

    # Initialize the AioPyFCM object.
    aiopyfcm_module = aiopyfcm.AioPyFCM()

    # Initialize the credentials from the JSON file. (Be required)
    aiopyfcm_module.init_credentials_from_file(
        credentials_file_path="<your_credentials_path>/credentials.json",
        auto_refresh=True  # Default is True
    )

    return aiopyfcm_module


async def credentials_sample_2():
    """
    This example demonstrates how to authenticate by converting the contents of a JSON file into a <Dict> or <String>.
    """
    credentials_dict = {
        "type": "service_account",
        "project_id": "837477-Sample",
        "private_key_id": "XXXX...",
        "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-XXXX...",
        "client_id": "XXXX...",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-XXXX...",
        "universe_domain": "googleapis.com"
    }
    credentials_dumps = json.dumps(credentials_dict)

    # Initialize the AioPyFCM object.
    aiopyfcm_module = aiopyfcm.AioPyFCM()

    # Initialize the credentials from the <Dict> or <JSON string>. (Be required)
    aiopyfcm_module.init_credentials(
        credentials=credentials_dict or credentials_dumps,
        auto_refresh=True  # Default is True
    )

    return aiopyfcm_module


async def send_stateful_sample():
    """
    This sample is used when you want to maintain an asynchronous session of aiohttp.
    You can use resources efficiently by not opening a session every time you send.
    """

    # Initialize the AioPyFCM object.
    aiopyfcm_module = await credentials_sample_1()

    # Create a message object.
    message = {
        "notification": {
            "title": "Sample Title",
            "body": "Sample Body",
            "image": "https://example.com/sample.jpg"
        }
    }

    # Send the message. (Stateful - Recommended)
    async with aiopyfcm_module as async_fcm:
        responses = await asyncio.gather(
            async_fcm.send(message),
            async_fcm.send(message),
            async_fcm.send(message),
        )
        print(responses)


async def send_stateless_sample():
    """
    This sample uses the AsyncPyFCM object by declaring it.
    This method does not maintain the aiohttp asynchronous session,
    so it connects the session every time you send.
    """

    # Initialize the AioPyFCM object.
    aiopyfcm_module = await credentials_sample_1()

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
        aiopyfcm_module.send(message),
        aiopyfcm_module.send(message),
        aiopyfcm_module.send(message),
    )
    print(responses)

```

## Contributing
The following is a set of guidelines for contributing to `aiopyfcm`. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

1. Please create a branch in this format, **`<Issue Number>-<Some name>`**
2. Open a terminal and navigate to your project path. And enter this.
   **`git config --global commit.template .gitmessage.txt`**
3. You can use the template, with `git commit` through vi. **Not** `git commit -m`
4. If you want to merge your work, please pull request to the `dev` branch.
5. Enjoy contributing!

If you have any other opinions, please feel free to suggest 😀

## License

This project is licensed under the terms of the MIT license.
