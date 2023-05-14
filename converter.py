def main():
    again = 'y'
    while again == 'y' or again == 'yes':
        kilo = float(input("Enter a distance in Kilometers: "))
        convert(kilo)
        again = input("Do you want to perform that again? Enter 'y' for yes: ")


def convert(n):
    miles = n * 0.6214
    print(f"The distance you entered from km to miles is {miles:.2f} miles")


main()
