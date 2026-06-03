"""
ATM Simulator

Author: Danilo Vunza
Course: COSC 1436

Description:
A simple ATM simulator that allows
users to check balance, deposit money,
withdraw funds, and exit the system.
"""


def display_menu():

    print("\n" + "=" * 40)
    print("ATM SIMULATOR")
    print("=" * 40)

    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    print("=" * 40)


def check_balance(balance):

    print(f"\nCurrent Balance: ${balance:.2f}")


def deposit(balance):

    while True:

        try:

            amount = float(
                input("Enter deposit amount: $")
            )

            if amount <= 0:

                print(
                    "Amount must be greater than zero."
                )

            else:

                balance += amount

                print(
                    f"Successfully deposited ${amount:.2f}"
                )

                return balance

        except ValueError:

            print("Invalid input.")


def withdraw(balance):

    while True:

        try:

            amount = float(
                input("Enter withdrawal amount: $")
            )

            if amount <= 0:

                print(
                    "Amount must be greater than zero."
                )

            elif amount > balance:

                print(
                    "Insufficient funds."
                )

            else:

                balance -= amount

                print(
                    f"Successfully withdrew ${amount:.2f}"
                )

                return balance

        except ValueError:

            print("Invalid input.")


def main():

    balance = 1000.00

    while True:

        display_menu()

        choice = input(
            "Select an option (1-4): "
        )

        if choice == "1":

            check_balance(balance)

        elif choice == "2":

            balance = deposit(balance)

        elif choice == "3":

            balance = withdraw(balance)

        elif choice == "4":

            print(
                "\nThank you for using ATM Simulator."
            )

            break

        else:

            print(
                "\nInvalid option. Please try again."
            )


main()
