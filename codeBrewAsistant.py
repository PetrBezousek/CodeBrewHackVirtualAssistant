
def answerHello(inpt, user):
    if inpt.startswith( '@codeBrewAsistant' ):
        return f'Hello {user}'

def whereIs(inpt, location):
    strip_codeBrewAsistant = inpt.strip("@codeBrewAsistant")
    finaloutput = strip_codeBrewAsistant.strip(" where is ")
    return f'{finaloutput} is in {location}'

def whenIsFree(inpt, time):
    # print(inpt)
    strip_codeBrewAsistant = inpt.strip("@codeBrewAsistant")
    finaloutput = strip_codeBrewAsistant.strip(" when is free ")

    return f'{finaloutput} is free at {time}'

print(answerHello('@codeBrewAsistant ', 'Miro'))
print(whereIs('@codeBrewAsistant where is Marek', 'New York'))
print(whenIsFree('@codeBrewAsistant when is free Marek', 10))