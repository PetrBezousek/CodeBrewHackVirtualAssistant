import requests
from config import token_bot, token_god
from datetime import datetime, time, timezone

def get_midnight_timestamp():
    midnight = datetime.combine(datetime.now().date(), time(0,0))
    timestamp = midnight.replace(tzinfo=timezone.utc).timestamp()
    return str(midnight.timestamp())

def post_message(params):
    '''
    params:
    {
        channel
        text
    }
    '''
    params['token'] = token_bot
    api_url = 'https://slack.com/api/chat.postMessage'

    resp = requests.get(api_url, params)
    print(resp.text)

    return resp

def get_messages(params):
    '''
    {
        channel
    }
    '''
    api_url = 'https://slack.com/api/channels.history'

    params['token'] = token_god
    params['oldest'] = get_midnight_timestamp()

    resp = requests.get(api_url, params)
    print(resp.text)

    return resp
