def is_even(number):
    if (number % 2) == 0:
        status = True
    else:
        status = False

    return status


number = float(input("Enter a number: "))

if is_even(number):
    print("Number is even")

else:
    print("Number is odd")
