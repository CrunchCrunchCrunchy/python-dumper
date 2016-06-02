import re, pyperclip
text=pyperclip.paste()
emailregex=re.compile(r'[A-Za-z0-9]*@[A-Za-z0-9]*')
match=emailregex.findall(text)
print(match)
