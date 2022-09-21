# A travel expenses calculator
# 9/21/2022
# CTI-110 P1HW2 - Travel Expense
# Kayla Smith
#

# Input Float budget
# Input location
# Input Float gas
# Input Float accomodation
# Input Float food
# 
# Set total to gas + accomodation + food
# Set balance to budget - total
#
# Display blank
# Display travel expenses header
# Display location
# Display budget
# Display blank
# Display gas
# Display accomodation
# Display food
# Display blank
# Display balance

# Input
budget = float(input('Enter your budget > '))
location = input('Enter your travel destination > ')
gas = float(input('How much do you think you will spend on gas? > '))
accomodation = float(input('How much will you need for accomodation/hotel? > '))
food = float(input('How much will you spend on food? > '))
# Process
total = gas + accomodation + food
balance = budget - total
# Output
print()
print('------------Travel Expenses------------')
print('Location: ', location)
print('Initial budget: ', budget)
print()
print('Fuel: ', gas)
print('Accomodation: ', accomodation)
print('Food: ', food)
print()
print('Remaining Balance: ', balance)
