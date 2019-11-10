import requests
from config import token_bot, token_god
from datetime import datetime, time, timezone
import json
import dateutil.parser
import pytz


def get_dt(strng):
    return dateutil.parser.parse(strng)

def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    utc=pytz.UTC
    # start = utc.localize(start.replace(tzinfo=utc))
    # end = utc.localize(end).replace(tzinfo=utc)
    x = x.astimezone(pytz.utc).replace(tzinfo=None)
    start = start.astimezone(pytz.utc).replace(tzinfo=None)
    end = end.astimezone(pytz.utc).replace(tzinfo=None)

    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

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
            dict[message['username']] = {'ts':message['ts'],'text':message['text']}
        elif message.get('user') and message['user'] not in dict.keys():
            dict[message['user']] = {'ts':message['ts'],'text':message['text']}

    if user:
        for id, text in dict.items():
            print(id, ' == ', user)
            if id == user and not text['text'].endswith('has joined the channel'):
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

def getEventNow(email):
    if email == None:
        return False

    url = "https://api.kloudless.com/v1/accounts/345949153/cal/calendars"

    querystring = {"":""}

    headers = {
            'Authorization': "ApiKey oUXqY2YbHHTbejR0yU6eOhNICU_i68lCUfNMe1hGTGurHGrx",
            'User-Agent': "FrajerCrawler 420.69",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "2ef0a8e9-4a63-4438-b096-11296d10d421,55b6bbed-e08f-4ae0-b59c-52c0e8a16f17",
            'Host': "api.kloudless.com",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    c_data = json.loads(response.text)

    found = False

    for calendar in c_data['objects']:
        if calendar['name'] == email:
            found = calendar

    if found == False:
        return False

    url = f"https://api.kloudless.com/v1/accounts/345949153/cal/calendars/{found['id']}/events"

    querystring = {
            "start":datetime.now().replace(microsecond=0).isoformat(),
            "end":datetime.combine(datetime.now().date(), time(23,59)).isoformat()
        }

    headers = {
            'Authorization': "ApiKey oUXqY2YbHHTbejR0yU6eOhNICU_i68lCUfNMe1hGTGurHGrx",
            'User-Agent': "PostmanRuntime/7.17.1",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "025353cd-c527-4573-98de-05659c487843,55a37761-8ca7-4823-a625-6af34520fa56",
            'Host': "api.kloudless.com",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    events = json.loads(response.text)['objects']

    now_running = []
    for e in events:
        start = get_dt(e['start'])
        end = get_dt(e['end'])
        if time_in_range(start, end, datetime.now()):
            now_running.append(e)
    msg = []
    for e in now_running:
        a_day = 'All day event' if e['all_day'] else 'Event'
        xd = f'{a_day} {e["name"]} ending {e["end"]}'
        msg.append(xd)
    return '\n'.join(msg)

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
