def main():
    # Get the user's age
    u_age = int(input("Enter your age: "))
    # Get user's friend's age
    f_age = int(input("Enter your friend's age: "))
    # Sum of both user and friend's age
    # The sum function has been called in the main function
    total = sum(u_age, f_age)
    # Display the sum of their ages
    print(f"The sum of your ages is {total}")


def sum(num1, num2):
    return num1 + num2


#  Call the main() functions
main()
