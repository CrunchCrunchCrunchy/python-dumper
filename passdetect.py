text=input('Enter password to test, press enter for clipboard\n')
import re
if text=='':
    import pyperclip
    text=pyperclip.paste()
def numofchar(text):
    if len(text)>8:
        return True
    else:
        return False
def Ul(text):
    ulregex=re.compile(r'[a-z]|[A-Z]')
    mo=ulregex.search(text)
    if mo:
        return True
    else:
        return False
def digit(text):
    digitregex=re.compile(r'[0-9]')
    mo=digitregex.search(text)
    if mo:
        return True
    else:
        return False
def masterpass(text):
    if (numofchar(text)and Ul(text) and digit(text)):
        return True
    else:
        return False
if masterpass(text):
    print('this is a valid password')
else:
    print('this is NOT a valid password')
