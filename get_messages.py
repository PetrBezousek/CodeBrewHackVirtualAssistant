import requests

token = 'xoxp-830034645303-827714821620-830112343751-d6683c335cdabe0d0779a90fc9599f32'
endpoint = 'https://slack.com/api/channels.history'
# channels:history

response = requests.get('https://slack.com/api/channels.history?token={0}&channel=CQC5H8W6R&pretty=1'.format(token))
print(response.text)