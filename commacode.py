mylist=[]
finlist=''
print('Enter first value')
mylist=[input()]
while mylist[-1] !='':
    print('Enter new value, press enter to end list.')
    mylist.append(input())
del mylist[-1]
x=str(mylist[-1])
def listprint():
    global mylist
    global finlist
    while len(mylist)>1:
        finlist= finlist+ str(mylist[0]+', ')
#        print(mylist[0]+',')
        del mylist[0]
listprint()
print(finlist+ 'and ' +x)
