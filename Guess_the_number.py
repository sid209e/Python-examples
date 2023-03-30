# This is a guess the number game
# You have to guess a number between 1 and 20
import random
secretnum = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20")

# Ask the user to guess 6 times
for guessesTaken in range(1,7):
    print('Guess the number.')
    guess = int(input())
    
    if guess < secretnum:
        print('Uh-oh! Too low.')
    elif guess > secretnum:
        print('Uh-oh! Too high.')
    else:
        break  # This condition is the correct guess
    
if guess == secretnum:
    print('Yay! your guess is correct. You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was' + str(secretnum))