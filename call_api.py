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

def get_messages(params, user=None):
    '''
    {
        channel
    }
    '''
    api_url = 'https://slack.com/api/channels.history'

    params['token'] = token_god
    params['oldest'] = get_midnight_timestamp()

    resp = json.loads(requests.get(api_url, params).text)

    dict = {}

    for message in resp['messages']:

        try:
            if message.get('username'):
                dict[message['username']].append(message['text'])
            elif message.get('user'):
                dict[message['user']].append(message['text'])
        except KeyError:
            if message.get('username'):
                dict[message['username']] = [message['text']]
            elif message.get('user'):
                dict[message['user']] = [message['text']]

    print(dict)

    return dict


def get_channels():

    api_url = 'https://slack.com/api/channels.list'

    params = {'token': token_god, 'pretty':1}

    resp = json.loads(requests.get(api_url, params).text)

    channels = []
    for channel in resp['channels']:
        channels.append({channel['id']: channel['name']})

    print(channels)
    return channels

def get_users(uname_first=False, name=False):

    api_url = 'https://slack.com/api/users.list'

    params = {'token': token_god, 'pretty': 1}

    resp = json.loads(requests.get(api_url, params).text)

    users = {}
    if uname_first or name:
        if name:
            userdata = ''

            for user in resp['members']:
                if user['name'] == name:
                    userdata = {user['name']:user['id']}

            return userdata

        for user in resp['members']:
            users[user['name']] = user['id']
    else:
        for user in resp['members']:
            users[user['id']] = user['name']

    print(users)
    return users