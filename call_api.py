import requests
from config import token_bot, token_god
from datetime import datetime, time, timezone
import json

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


def get_channels():

    api_url = 'https://slack.com/api/channels.list'

    params = {'token': token_god, 'pretty':1}

    resp = json.loads(requests.get(api_url, params).text)

    channels = []
    for channel in resp['channels']:
        channels.append({channel['id']: channel['name']})

    print(channels)
    return channels

def get_users():
    api_url = 'https://slack.com/api/users.list'

    params = {'token': token_god, 'pretty': 1}

    resp = json.loads(requests.get(api_url, params).text)

    users = []
    for user in resp['members']:
        users.append({user['id']: user['name']})

    print(users)
    return users

get_users()

