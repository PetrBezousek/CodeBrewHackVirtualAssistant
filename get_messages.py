import requests
from config import token_god

endpoint = 'https://slack.com/api/channels.history'
# channels:history

response = requests.get('https://slack.com/api/channels.history?token={0}&channel=CQC5H8W6R&pretty=1'.format(token_bot))
print(response.text)