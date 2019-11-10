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
        if message.get('username') and message['username'] not in dict.keys():
            dict[message['username']] = [message['text']]
        elif message.get('user') and message['user'] not in dict.keys():
            dict[message['user']] = [message['text']]

    if user:
        for id, text in dict.items():
            print(id, ' == ', user)
            if id == user and not text[0].endswith('has joined the channel'):
                print(text)
                return text

    else:
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
            print(user)

    print(users)
    return users


def get_email(id):

    api_url = 'https://slack.com/api/users.list'

    params = {'token': token_god, 'pretty': 1}

    resp = json.loads(requests.get(api_url, params).text)

    for user in resp['members']:
        if user['id'] == id:
            print(user['profile']['email'])
            return user['profile']['email']
    else:
        return None
