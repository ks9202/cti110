# A math quiz with a menu where the user can be asked
# simple addition or subtraction problems.
# 11/28/2022
# CTI-110 P5HW2 - Math Quiz
# Kayla Smith
#

# Import menu and random math.
import Menu
import RandomMath

# Menu loop, calls functions to print the menu and questions.
exitProgram = False
while exitProgram == False:
    print('')
    Menu.displayMenu()
    choice = input('Please choose one of the menu options: ')
    print('')
    if choice == '1':
        RandomMath.addition()
    elif choice == '2':
        RandomMath.subtraction()
    elif choice == '3':
        exitProgram = True
    else:
        print('Invalid choice. Please select 1, 2, or 3.')

# Termination message.
print('Thank you for playing...')
print('Bye!!')
