from typing import TypedDict, Optional


class Notification(TypedDict):
    """
    Notification
    https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#Notification
    """
    title: str
    body: str
    image: str


class LightSettings(TypedDict):
    """
    Light Settings
    https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#LightSettings
    """
    color: dict
    light_on_duration: str
    light_off_duration: str


class AndroidNotification(TypedDict):
    """
    Android Notification
    https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#AndroidNotification
    """
    title: str
    body: str
    icon: str
    color: str
    sound: str
    tag: str
    click_action: str
    body_loc_key: str
    body_loc_args: list[str]
    title_loc_key: str
    title_loc_args: list[str]
    channel_id: str
    ticker: str
    sticky: bool
    event_time: str
    local_only: bool
    notification_priority: str
    default_sound: bool
    default_vibrate_timings: bool
    default_light_settings: bool
    vibrate_timings: list[str]
    visibility: str
    notification_count: int
    light_settings: LightSettings
    image: str


class AndroidFcmOptions(TypedDict):
    """
    Android FCM Options
    https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#AndroidFcmOptions
    """
    analytics_label: str


class AndroidConfig(TypedDict):
    """
    Android Config
    https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#AndroidConfig
    """
    collapse_key: str
    priority: str
    ttl: str
    restricted_package_name: str
    data: dict[str, str]
    notification: AndroidNotification
    fcm_options: AndroidFcmOptions
    direct_boot_ok: bool


class WebpushFcmOptions(TypedDict):
    """
    Webpush FCM Options
    https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#WebpushFcmOptions
    """
    link: str
    analytics_label: str


class WebpushConfig(TypedDict):
    """
    Webpush Config
    https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#WebpushConfig
    """
    headers: dict[str, str]
    data: dict[str, str]
    notification: dict
    fcm_options: WebpushFcmOptions


class ApnsFcmOptions(TypedDict):
    """
    APNS FCM Options
    https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#ApnsFcmOptions
    """
    analytics_label: str
    image: str


class ApnsConfig(TypedDict):
    """
    APNS Config
    https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#ApnsConfig
    """
    headers: dict[str, str]
    payload: dict
    fcm_options: ApnsFcmOptions


class FcmOptions(TypedDict):
    """
    FCM Options
    https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#FcmOptions
    """
    analytics_label: str


class Message(TypedDict):
    """
    FCM Message Resource
    https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages
    """
    token: str
    name: Optional[str]
    data: Optional[dict[str, str]]
    notification: Optional[Notification]
    android: Optional[AndroidConfig]
    webpush: Optional[WebpushConfig]
    apns: Optional[ApnsConfig]
    fcm_options: Optional[FcmOptions]
    topic: Optional[str]
    condition: Optional[str]
