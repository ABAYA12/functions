# Returning the square root of a number

# set a priming read
import math


def main():
    again = "y"
    while again == "y" or again == 'yes':
        # Get a number from the user
        number = int(input("Enter a number: "))
        # Return the square root of the number
        result = math.sqrt(number)
        # Display the result
        print(f"The square root of {number} is {result}")

        again = str(
            input("Do you want to perform that again? Enter 'y' for yes: "))


main()
