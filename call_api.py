import requests
from config import token

def call_slack_api(method, scope, params=[]):
    api_url = 'https://slack.com/api/'

    params = '&'.join(params)
    if params:
        params = '?' + params

    if method == "POST":
        resp = requests.post('{url}{scope}{params}'.format(url=api_url,
                                                           scope=scope,
                                                           params=params))
    if method == "GET":
        resp = requests.post('{url}{scope}{params}'.format(url=api_url,
                                                           scope=scope,
                                                           params=params))                                                       
    print(resp.text)

# TEST volani
# params = ['channel=CQC5H8W6R', 'text=HelloWorld!', 'token={token}'.format(token=token)]
# call_slack_api("POST", "chat.postMessage", params)
