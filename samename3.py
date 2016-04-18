def spam():
    global eggs
    eggs='spam' # this is the global
def bacon():
    eggs= 'bacon' #this is the global
def ham():
    print(eggs) # this is global


eggs= 42 #is global
spam()
print(eggs)
