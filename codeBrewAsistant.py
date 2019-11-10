from call_api import *
from random import choice
from flask import jsonify


def answerHello(inpt, user):
    if inpt.startswith( '@codeBrewAsistant' ):
        return f'Hello {user}'

def whereIs(inpt, seeker):
    for word in inpt.split(' '):
        if word.startswith('@'):
            print(get_users(name=word[1:]))
            user = get_users(name=word[1:])
    print(user)

    usr_key = None
    for k,v in user.items():
        usr_key = k
    if user:
        p = None
        for k,v in user.items():
            p = v
        m = get_messages({'channel': 'CQEPDT1GE'}, user=p)
        if type(m) == list:
            m = m[0]

        if m:
            return f'@{usr_key} \n> {m}'
        else:
            post_message({'text': f"Hi, {seeker} is looking for you. PRO TIP: next time, you can write message in #iamlate and I will automaticly respond to him.", 'channel': p})
            return "No message found in #iamlate. I told him you are looking for him."
    return "I did not find this user."

def whereIsWaldo():
    waldoList = [
        'https://i.imgur.com/ON0bOGCh.jpg',
        'https://i.imgur.com/22xeBboh.jpg',
        'https://i.imgur.com/wH9f8nTh.jpg',
        'https://i.imgur.com/fYARp5kh.jpg',
        'https://i.imgur.com/7mPombrh.jpg',
        'https://i.imgur.com/1swVnrvh.jpg',
        'https://i.imgur.com/DMXKainh.jpg',
        'https://i.imgur.com/s6BDAMYh.jpg',
        'https://i.imgur.com/CMhMAlEh.jpg',
        'https://i.imgur.com/lkdEmh3h.jpg',
        'https://i.imgur.com/5ROvxWph.jpg',
        'https://i.imgur.com/UQpjRPah.jpg',
        'https://i.imgur.com/k7rBC7Nh.jpg',
        'https://i.imgur.com/56LEadSh.jpg',
        'https://i.imgur.com/iYbQPAkh.jpg',
        'https://i.imgur.com/xTsstgZh.jpg',
        'https://i.imgur.com/yOgPZh6h.jpg',
        'https://i.imgur.com/YdH3CRgh.jpg',
        'https://i.imgur.com/RMq8w60h.jpg',
        'https://i.imgur.com/txDhaJOh.jpg',
        'https://i.imgur.com/UAELJLFh.jpg',
        'https://i.imgur.com/5e3xsy3h.jpg',
        'https://i.imgur.com/qPzrnnvh.jpg',
        'https://i.imgur.com/QGb8s8fh.jpg'
    ]

    return choice(waldoList)

def whenIsFree(inpt, time):
    strip_codeBrewAsistant = inpt.strip("@codeBrewAsistant")
    finaloutput = strip_codeBrewAsistant.strip(" when is free ")
    return f'{finaloutput} is free at {time}'

def format_response(response):
    '''
        Make a json
    '''
    response_type = type(response)
    if response_type == dict:
        return jsonify(response)
    elif response_type == str:
        return jsonify(text=response)
    else:
        return jsonify(text="Something went wrong.")

def format_txt(text):
    '''
        Transform "  Where Is WALdo ??  " to "where is waldo ??"
    '''
    return text.lower().strip()