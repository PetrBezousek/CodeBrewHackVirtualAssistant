import requests

token = 'xoxp-830034645303-827714821620-816768327875-cdc25b44c301a3ae2a00abb691c6da92'
endpoint = 'https://slack.com/api/channels.history'
# channels:history

response = requests.get('https://slack.com/api/channels.history?token={0}&channel=CQC5H8W6R&pretty=1'.format(token))
print(response.text)