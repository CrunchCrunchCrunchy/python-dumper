# this is a guses the number game
import random
secretnumber=random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

#Ask the player to guess six times
for guessestaken in range(1,7):
    print('Take a guess')
    guess =int(input())

    if guess < secretnumber:
        print('Your guess is too low')
    elif guess > secretnumber:
        print('Your guess is too high')
    else:
        break # this means it was the correct guess

if guess== secretnumber:
    print('Good job! You guessed the number in '+str(guessestaken) + ' guesses!')
else: print('Nope, my number was ' + str(secretnumber)+ '!')
