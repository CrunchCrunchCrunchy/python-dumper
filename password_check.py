realpassword='yea'
realname='Jarod'
print('What is your name')
name=input()
if name==realname :
        print('Password?')
        enteredpassword=input()
        if enteredpassword==realpassword:
                print('Access Granted')
        if enteredpassword!=realpassword:
            print('Denied')
if name!=realname :
    print('Denied')
