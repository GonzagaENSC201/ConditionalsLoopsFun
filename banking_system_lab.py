# Note: Professor Colburn's lab, copied as is 10/7/26

"""Loops File 2: Build a simple banking system.

You will write three small functions. Each function takes the current balance
as a parameter and RETURNS a result; it does not print.
main() (provided) is a menu loop that asks the user what to do and calls
your functions. run_test_cases() calls each function with simple test cases.

WORKFLOW FOR EVERY STEP
1. Read the docstring and the "Expected" examples.
2. Write a prediction of what your function should do for one example.
3. Replace the "TODO" with working code.
4. Run the file, choose menu option 5 (run test cases), and compare each
   result with the expected value. Then try the function from the menu.
5. If a result is wrong, set a breakpoint inside your function and step through.
"""


# STEP 1: Deposits (a worked example - read it, then run it)
def deposit(balance, amount):
    """Return the new balance after depositing amount.

    A deposit must be greater than zero. Otherwise the balance is unchanged.
    Expected: deposit(100, 50) -> 150      deposit(100, -20) -> 100
    """
    if amount > 0:
        balance = balance + amount
    return balance


# STEP 2: Withdrawals (conditionals, like last week)
def withdraw(balance, amount):
    """Return the new balance after withdrawing amount.

    The withdrawal is allowed only if amount is greater than zero AND amount
    is not more than the balance. Otherwise the balance is unchanged.
    Expected: withdraw(100, 30) -> 70    withdraw(100, 150) -> 100
              withdraw(100, 100) -> 0    withdraw(100, -5) -> 100
    """
    # TODO: write the conditional, update balance when allowed, then return it.
    return balance


# STEP 3: A for loop with an accumulator
def balance_after_interest(balance, rate, years):
    """Return the balance after adding interest once per year.

    Each year, balance becomes balance + balance * rate.
    Expected: balance_after_interest(1000, 0.05, 2) -> 1102.5
              balance_after_interest(1000, 0.05, 0) -> 1000
    Hint: for year in range(years): ... update balance inside the loop.
    """
    # TODO: write a for loop that updates balance once per year.


# STEP 4: Write a message that reports an account summary
def account_summary(name, balance):
    """Return a one-line message with the account holder and balance.

    Expected: account_summary("Ada", 140) -> "Ada's balance is $140.00"
    Hint: use an f-string and format the balance with :.2f.
    """
    # TODO: return the formatted message.
    return "TODO"


def run_test_cases():
    """Call each banking function with simple test cases."""
    print("Deposit:", deposit(100, 50))
    print("Withdraw:", withdraw(100, 30))
    print("Overdraw attempt:", withdraw(100, 150))
    print("With interest:", balance_after_interest(1000, 0.05, 2))
    print(account_summary("Ada", 140))


def show_menu():
    """Print the menu of choices."""
    print()
    print("===== ENSC BANK =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Project balance with interest")
    print("4. Account summary")
    print("5. Run test cases")
    print("6. Quit")


def main():
    """PROVIDED: the user interface. Read it, but you do not need to edit it.

    A while loop keeps showing the menu until the user chooses Quit.
    Each choice asks for the information it needs, calls one of your
    functions, and prints what the function returned.
    """
    name = input("Account holder name: ")
    balance = float(input("Starting balance: "))
    choice = ""

    while choice != "6":
        show_menu()
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            amount = float(input("Deposit amount: "))
            balance = deposit(balance, amount)
            print("New balance:", balance)
        elif choice == "2":
            amount = float(input("Withdrawal amount: "))
            balance = withdraw(balance, amount)
            print("New balance:", balance)
        elif choice == "3":
            rate = float(input("Yearly interest rate (0.05 = 5%): "))
            years = int(input("Number of years: "))
            print("Balance after interest:", balance_after_interest(balance, rate, years))
        elif choice == "4":
            print(account_summary(name, balance))
        elif choice == "5":
            run_test_cases()
        elif choice == "6":
            print("Thank you for banking with us, " + name + "!")
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


# EXTENSIONS (optional) - write each function, add a call to run_test_cases(),
# then add a menu option for it in show_menu() and main().
#
# 1. process_transactions(balance, transactions)  [for loop]
#    Return the balance after applying every number in the list. A positive
#    number is a deposit and a negative number is a withdrawal. A withdrawal
#    that would overdraw the account is skipped.
#    Expected: process_transactions(100, [50, -30, 20]) -> 140
#              process_transactions(100, [-150, 25]) -> 125
#    Hint: call deposit() and withdraw(balance, -amount).
#    Menu input: text = input("Transactions: "); then
#    [float(item) for item in text.split()] makes the list.
#
# 2. months_to_reach_goal(balance, goal, monthly_deposit)  [while loop]
#    Return the number of months until balance reaches goal, adding
#    monthly_deposit each month. Return 0 if the goal is already met.
#    Expected: months_to_reach_goal(100, 400, 100) -> 3
#              months_to_reach_goal(500, 400, 100) -> 0
#    Hint: keep a months counter and use: while balance < goal:
#
# 3. pin_attempts_message(pins_entered, correct_pin)  [while loop]
#    Check the PINs in the list in order, allowing at most 3 attempts.
#    Return "Access granted after N attempt(s)" at the first match, or
#    "Account locked" if none of the first 3 match.
#    Expected: pin_attempts_message([1111, 1234], 1234) -> "Access granted after 2 attempt(s)"
#              pin_attempts_message([1, 2, 3, 1234], 1234) -> "Account locked"
#    Hint: while attempts < 3 and attempts < len(pins_entered):
#
# 4. overdraft_fee(balance): return the balance minus a $5 fee if the
#    balance is below zero.
#
# 5. Make main() reject a non-numeric amount instead of crashing
#    (hint: str.isdigit() or try/except if you have seen it).


# CHECK-OUT QUESTIONS
# 1. Why does each function return the new balance instead of printing it?
# 2. What test cases did you use for the boundaries (zero, exact balance)?
# 3. How did a breakpoint help you fix one of your functions?
# 4. In main(), what condition ends the menu loop? What would happen if
#    no menu option ever set choice to "6"?


if __name__ == "__main__":
    main()
