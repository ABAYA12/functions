def main():
    again = 'y'  # Set a priming read
    while again == 'y' or again == 'yes':
        print("Enter your monthly expenses on the following:")
        # menu()
        loan = float(input("Enter loan payment per month: "))
        insurance = float(input("Enter insurance per month: "))
        oil = float(input("Enter amount spent on oil per month: "))
        gas = float(input("Enter amount spent on gas per month: "))
        tires = float(input("Enter amount spent on tires per month: "))
        maintenance = float(
            input("Enter amount spent on maintenance per month: "))
        print("Name of expense\tMonthly Expense\tAnnual Expense", sep=" ")
        print("Loan payment\nInsurance\nOil\nGas\nTires\nMaintenance")


main()
