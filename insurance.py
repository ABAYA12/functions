# How Much Insurance?
def main():
    mini_pay()
    print("This would be used to put back the structure incase of any incident")


def mini_pay():
    rate = 0.8
    amount = float(
        input("How much did it cost you to put up the whole building?: "))
    insurance = rate * amount
    print(f"The amount to pay as insuarnce is GHS{insurance:.2f}")


main()
