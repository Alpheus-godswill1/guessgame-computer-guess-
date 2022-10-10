import random 

def guessNum(n):
    random_number = random.randint(2, n)
    guessValue = 0
    while guessValue != random_number:
        guessValue = int(input(f'Guess a number between 2 and {n}: '))
        if guessValue > random_number:
            print('Hey pal, sorry you guess was too high, try again!')
        elif guessValue < random_number:
            print('Hey pal, sorry you guess was too low, try again!')
    print('Wow, you finally got the right answer, keep it up!')
guessNum(8)