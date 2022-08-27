from random import randint
from time import sleep
random_number = randint(0, 10)
trials_count = 0
colors = {'red': '\033[31m', 'green': '\033[32m', 'clear': '\033[m'}
print('=' * 17 + ' Guess The Number ' + '=' * 17)
print("Computer: I'm thinking on a number between 0 and 10..")
sleep(2)
print("Computer: Done. Now it's your time to try and guess it!")
user_answer = int(input('Your answer: '))
trials_count += 1
print('Loading...')
sleep(1)
while user_answer != random_number:
    print(f'{colors["red"]}Wrong number!{colors["clear"]}')
    user_answer = int(input('Try again: '))
    trials_count += 1
    print('Loading...')
    sleep(1)
if user_answer == random_number:
    print(f'{colors["green"]}Right number!{colors["clear"]}')
    print(f'You needed a total of {trials_count} trials to guess the number.')
print('=' * 20 + ' GAME  OVER ' + '=' * 20)
