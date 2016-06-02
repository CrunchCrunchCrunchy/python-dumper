#* list goes here
#! python3
# bullet point adder - adds wikipedia bullet points to sthe start
#of each line on the clipboard
print('Make sure your list is in the clipboard. press any key to continue')
input()
import pyperclip
text=pyperclip.paste()

#seperate lines and add stars
lines=text.split('\n')
for i in range(len(lines)): # loop through all indexes in the lines list
    lines[i]='*'+' '+lines[i] # add star space to beggining of each line
text='\n'.join(lines)
pyperclip.copy(text)
