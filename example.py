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
