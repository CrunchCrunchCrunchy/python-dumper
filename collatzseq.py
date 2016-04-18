i=0
def collatz():
    global number
    if number < 1:
        print('Enter nonzero positive number!') 
    elif number%2 == 0:
        number= float(number/2)
        return number
    elif number%2 > 0:
         number=float(3*number+1)
         return number
print('Enter value.')
number=float(input())
while number >1 :
    collatz()
    print(float(number))
    i=i+int(1)
print('You have reached 1 in ' + str(i)+ ' steps!')
