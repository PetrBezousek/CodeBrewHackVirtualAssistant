import requests
from config import token

endpoint = 'https://slack.com/api/channels.history'
# channels:history

response = requests.get('https://slack.com/api/channels.history?token={0}&channel=CQC5H8W6R&pretty=1'.format(token))
print(response.text)