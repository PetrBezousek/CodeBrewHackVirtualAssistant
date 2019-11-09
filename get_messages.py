import requests

token = 'xoxp-830034645303-827714821620-816714109955-055b8d24972aa72fa9a3f735f1fd10b6'
endpoint = 'https://slack.com/api/channels.history'
# channels:history

response = requests.get('https://slack.com/api/channels.history?token={0}&channel=CQC5H8W6R&pretty=1'.format(token))
print(response.text)