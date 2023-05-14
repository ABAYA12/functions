import random

# setting constants for min ad max value
min = 1
max = 6

# set a priming read
again = 'y'

while again == 'y' or again == 'Y':
    print("Dice rolling")
    print("RESULTS:")
    for count in range(2):
        print(random.randint(min, max))
    again = input(
        "Do you want to roll dice again?, 'y' for yes and 'n' for no: ")


number = random.randrange(0, 100, 10)
print(number)
