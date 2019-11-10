from call_api import *
from random import choice
from flask import jsonify
from datetime import datetime


def answerHello(inpt, user):
    if inpt.startswith( '@codeBrewAsistant' ):
        return f'Hello {user}'

def whereIs(inpt, seeker):
    ppp = []
    for word in inpt.split(' '):
        if word.startswith('@'):
            print(get_users(name=word[1:]))
            fff = get_users(name=word[1:])
            ppp.append(fff)
    responses = []
    for usr in ppp:
        usr_key = None
        for k,v in usr.items():
            usr_key = k
        if usr:
            ooo = None
            p = None
            for k,v in usr.items():
                p = v
                ooo = getEventNow(get_email(v))


            print('2222222222')
            print(ooo)
            print('33333333333')
            if ooo:
                responses.append(f'Current events from {usr_key} calendar:\n {ooo}')
            m = get_messages({'channel': 'CQEPDT1GE'}, user=p)
            if type(m) == list:
                m = m[0]
                # sldfhsljdfjaksdbfjkbsadk TODO
            print('ljsjldshfjlhsdjlfhsdljfhljsdhfldsfj')
            print(m)
            if m:
                qq = m['text']
                ww = datetime.fromtimestamp(int(float(m['ts']))).strftime("%d. %m. %Y, %H:%M:%S")
                responses.append(f'`{ww}` @{usr_key} \n> {qq}')
            else:
                post_message({'text': f"Hi, {seeker} is looking for you. PRO TIP: next time, you can write message in #iamlate and I will automaticly respond to him.", 'channel': p})
                responses.append(f"No message from @{usr_key} found in #iamlate. I told him you are looking for him.")
    print('44444')
    if responses:
        print('55555')
        return '\n'.join(responses)
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