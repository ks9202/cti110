import random

# Asks a user a random addition problem with numbers 1-100.
def addition():
    # Get random numbers and answer, print question and prompt user
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    answer = num1 + num2
    print(f'  {num1}')
    print(f'+ {num2}')
    print('')
    print('Enter answer.')
    userAnswer = int(input())

    # Determines if a user's guess is correct, too low, or too high.
    # Loops until correct, and tracks number of guesses.
    guesses = 0
    correct = False
    while correct == False:
        if userAnswer > answer:
            guesses += 1
            print('Sorry, that guess is too high.')
            print('')
            userAnswer = int(input('Try again: '))
        elif userAnswer < answer:
            guesses += 1
            print('Sorry, that guess is too low.')
            print('')
            userAnswer = int(input('Try again: '))
        else:
            guesses += 1
            correct = True
    print('Congratulations!!! Your answer is correct.')
    print(f'Number of guesses: {guesses}')



# Asks a user a random subtraction problem with numbers 1-100.
def subtraction():
    # Get random numbers and answer, print question and prompt user
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    answer = num1 - num2
    print(f'  {num1}')
    print(f'- {num2}')
    print('')
    print('Enter answer.')
    userAnswer = int(input())

    # Determines if a user's guess is correct, too low, or too high.
    # Loops until correct, and tracks number of guesses.
    guesses = 0
    correct = False
    while correct == False:
        if userAnswer > answer:
            guesses += 1
            print('Sorry, that guess is too high.')
            print('')
            userAnswer = int(input('Try again: '))
        elif userAnswer < answer:
            guesses += 1
            print('Sorry, that guess is too low.')
            print('')
            userAnswer = int(input('Try again: '))
        else:
            guesses += 1
            correct = True
    print('Congratulations!!! Your answer is correct.')
    print(f'Number of guesses: {guesses}')
