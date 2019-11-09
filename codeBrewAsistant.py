from call_api import *

def answerHello(inpt, user):
    if inpt.startswith( '@codeBrewAsistant' ):
        return f'Hello {user}'

def whereIs(inpt, location):
    for word in inpt.split(' '):
        if word.startswith('@'):
            print(get_users(name=word[1:]))
            user = get_users(name=word[1:])

    return f'{word} is in {location}' if user else "User Not Found :("

def whenIsFree(inpt, time):
    strip_codeBrewAsistant = inpt.strip("@codeBrewAsistant")
    finaloutput = strip_codeBrewAsistant.strip(" when is free ")
    return f'{finaloutput} is free at {time}'

print(whereIs('where is @geletamarek', 'New York'))
