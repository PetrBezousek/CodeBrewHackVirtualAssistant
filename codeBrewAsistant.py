from call_api import *
from random import choice
def answerHello(inpt, user):
    if inpt.startswith( '@codeBrewAsistant' ):
        return f'Hello {user}'

def whereIs(inpt, location):
    for word in inpt.split(' '):
        if word.startswith('@'):
            print(get_users(name=word[1:]))
            user = get_users(name=word[1:])

    return f'{word} is in {location}' if user else "User Not Found :("

def whereIsWaldo():
    waldoList = ['https://i.imgur.com/ON0bOGC.jpg', 'https://i.imgur.com/22xeBbo.jpg', 'https://i.imgur.com/wH9f8nT.jpg', 'https://i.imgur.com/fYARp5k.jpg', 'https://i.imgur.com/7mPombr.jpg', 'https://i.imgur.com/1swVnrv.jpg', 'https://i.imgur.com/DMXKain.jpg', 'https://i.imgur.com/s6BDAMY.jpg', 'https://i.imgur.com/CMhMAlE.jpg', 'https://i.imgur.com/lkdEmh3.jpg', 'https://i.imgur.com/5ROvxWp.jpg', 'https://i.imgur.com/UQpjRPa.jpg', 'https://i.imgur.com/k7rBC7N.jpg', 'https://i.imgur.com/56LEadS.jpg', 'https://i.imgur.com/iYbQPAk.jpg', 'https://i.imgur.com/xTsstgZ.jpg', 'https://i.imgur.com/yOgPZh6.jpg','https://i.imgur.com/YdH3CRg.jpg', 'https://i.imgur.com/RMq8w60.jpg', 'https://i.imgur.com/txDhaJO.jpg', 'https://i.imgur.com/UAELJLF.jpg', 'https://i.imgur.com/5e3xsy3.jpg', 'https://i.imgur.com/qPzrnnv.jpg', 'https://i.imgur.com/QGb8s8f.jpg']

    return choice(waldoList)

def whenIsFree(inpt, time):
    strip_codeBrewAsistant = inpt.strip("@codeBrewAsistant")
    finaloutput = strip_codeBrewAsistant.strip(" when is free ")
    return f'{finaloutput} is free at {time}'
