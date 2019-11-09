import requests
from datetime import datetime, time, timezone
import call_api


def get_midnight_timestamp():
    midnight = datetime.combine(datetime.now().date(), time(0,0))
    timestamp = midnight.replace(tzinfo=timezone.utc).timestamp()
    return midnight.timestamp()


def get_messages(channel='CQC5H8W6R',user=None):

    params = []
    scope = 'channels.history'
    oldest = str(get_midnight_timestamp())
    params.append('channel='+channel,'oldest='+oldest,'pretty=1')

    if user:
        params.append('user='+user)

    return call_api('GET',scope, params)


print(get_messages())



