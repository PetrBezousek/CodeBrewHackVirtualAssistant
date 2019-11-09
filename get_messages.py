import requests

token = 'xoxb-830034645303-830040044903-Cm8ZHXshO8QsPj2KUylifLb4'
endpoint = 'https://slack.com/api/channels.history'
# channels:history

response = requests.get('https://slack.com/api/channels.history?token={0}&channel=CQC5H8W6R&pretty=1'.format(token))
print(response.text)