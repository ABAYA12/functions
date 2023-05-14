# Import the circle and rectangle modules
import circle
import rectangle

Circle_Area = 1
Circle_Circum = 2
Rectangle_Area = 3
Rectangle_Peri = 4
Exit_pro = 5


def main():
    # Setting  a validating value to hold the while loop in this main func.
    choice = 0
    while choice != Exit_pro:
        # Display menu
        menu()
        choice = int(input("Enter your choice: "))
        if choice == Circle_Area:
            print("You are calculating the area of a circle")
            radius = float(input("Enter the radius of the circle: "))
            print(f"The area of the circle is {circle.area(radius):.2f}")

        elif choice == Circle_Circum:
            print("You are calculating the circumference of a circle")
            radius = float(input("Enter the radius of the circle: "))
            print(
                f"The circumference of the circle is {circle.circum(radius):.2f}")

        elif choice == Rectangle_Area:
            print("Youn are calculating the area of a rectangle")
            l = float(input("Enter length of the rectangle: "))
            b = float(input("Enter breath or width of the rectangle: "))
            print(f"The area of the rectangle is {rectangle.area(l, b):.2f}")

        elif choice == Rectangle_Peri:
            print("You are calculating the perimeter of a rectangle")
            l = float(input("Enter length of the rectangle: "))
            b = float(input("Enter breath or width of the rectangle: "))
            print(
                f"The perimeter of the rectangle is {rectangle.peri(l, b):.2f}")

        elif choice == Exit_pro:
            print("You have exited the program")
        else:
            print("Invalid choice")


def menu():
    print("""
    Enter (1) to calculate area of a circle
    Enter (2) to calcualte circumference of a circle
    Enter (3) to calculate the area of a rectangle
    Enter (4) to calculate the perimeter of a rectangle
    Enter (5) to quit the program
    """)


main()
