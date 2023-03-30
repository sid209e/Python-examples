# Rock, Paper, Scissors game
import random,sys

print("Rock, Paper, Scissors")

wins = 0
losses = 0
ties = 0
while True:
    print('%s Wins, %s Losses, %s Ties' %(wins, losses, ties))
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
        playerMove = input()
        if playerMove =='q':
            