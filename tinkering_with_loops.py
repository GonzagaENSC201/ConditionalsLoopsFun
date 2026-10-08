# Note: Professor Colburn's lab, adapted by Gina 10/7/26

"""Loops File 1: Tinker with for loops and while loops.

Use code tracing and breakpoints to see exactly what each loop does. Every
activity is a function that returns a value; main() prints labeled results.

THIS FILE HAS TWO PARTS
PART 1 - One example of each skill from our
         quizzes: code tracing, editing, test creation, and debugging.
         Finish all of Part 1 before you go deep on anything else.
PART 2 - Pick any of these to dig deeper. Do them in any
         order, but only after Part 1 is done.

HOW TO USE A BREAKPOINT IN VS CODE
1. Click in the gray margin to the left of a line number to set a red dot.
2. Run > Start Debugging (F5). Choose "Python File" if asked.
3. The program pauses on the breakpoint. Look at the VARIABLES panel.
4. F10 (Step Over) runs one line. F5 (Continue) runs to the next breakpoint.
5. Stop with Shift+F5.
Watch how the variables change each time the loop body repeats.

LAB ROUTINE FOR EVERY ACTIVITY
Predict -> Trace -> Debug -> Compare -> Explain
(Write your prediction in a comment before you run or debug the code.)
"""


# =========================================================================
# PART 1:
# =========================================================================

# CODE TRACING
# Trace this function by hand. Do NOT run it first.
#
# Fill in the table (the first rows are done for you):
#   pass | number | number % 2 == 1 ? | total after the pass
#   -----+--------+------------------+---------------------
#     1  |   1    |      True        |   1
#     2  |   2    |      False       |   1
#     3  |   3    |      ?           |   ?
#     4  |   4    |      ?           |   ?
#     5  |   5    |      ?           |   ?
#     6  |   6    |      ?           |   ?
#
# My prediction of what the function returns: ______
# Then put a breakpoint on "if number % 2 == 1:" and step through to check.
def sum_of_odds_to_six():
    """Return the sum of the odd numbers from 1 through 6."""
    total = 0
    for number in range(1, 7):
        if number % 2 == 1:
            total = total + number
    return total


# EDITING
# This function currently adds EVERY number from 1 through limit.
# EDIT it so it only adds the multiples of 3.
# Expected: sum_of_multiples_of_three(10) -> 18   (3 + 6 + 9)
#           sum_of_multiples_of_three(2)  -> 0
# Hint: use an if statement with the % operator, like Required 1.
def sum_of_multiples_of_three(limit):
    """Return the sum of the multiples of 3 from 1 through limit."""
    total = 0
    for number in range(1, limit + 1):
        total = total + number
    return total


# TEST CREATION
# count_above works. Your job is to write a unit test in test_tinkering_with_loops.py
# you can use the following example test case:
# 5 and 9 are above 4, so the answer is 2.
# assert count_above([1, 5, 9], 4) == 2
# TODO: add two more test cases
# Choose tests that are different from each other:
#   - a normal list
#   - an empty list
#   - a list with a value exactly equal to the cutoff (a boundary case)
# For each test, use an expected value YOU worked out by hand
# BEFORE running. 
def count_above(values, cutoff):
    """Return how many values are greater than cutoff."""
    count = 0
    for value in values:
        if value > cutoff:
            count = count + 1
    return count

# DEBUGGING
# It should total the list (answer 12 for [3, 4, 5]), but it does not.
# 1. Predict what it returns and why.
# 2. Put a breakpoint inside the loop and watch total in the VARIABLES panel.
# 3. Fix the bug, then explain the mistake in a comment.
def total_list_buggy(values):
    """Return the total of a list (contains a bug)."""
    for value in values:
        total = 0
        total = total + value
    return total


# =========================================================================
# PART 2: MORE PRACTICE
# =========================================================================

# PRACTICE A: A for loop with range()
# range(1, 5) produces 1, 2, 3, 4. It stops BEFORE the second number.
# Trace table (fill in the last two rows BEFORE running):
#   pass | number | total after the pass
#   -----+--------+---------------------
#     1  |   1    |   1
#     2  |   2    |   3
#     3  |   3    |   ?
#     4  |   4    |   ?
def sum_with_for_loop():
    """Return the sum of the numbers 1 through 4."""
    total = 0
    for number in range(1, 5):
        total = total + number
    return total


# Tinker: change range(1, 5) to range(1, 6), then to range(0, 5), then to
# range(5). Predict the total each time. How many passes does each make?


# PRACTICE B: Looping over a string and a list
# A for loop can take each item from a sequence, one at a time.
def count_letter_e(word):
    """Return how many times the letter e appears in word."""
    count = 0
    for letter in word:
        if letter == "e":
            count = count + 1
    return count


def average_of_list(measurements):
    """Return the average of a list of measurements."""
    total = 0
    for value in measurements:
        total = total + value
    average = total / len(measurements)
    return average


# Tinker: change count_letter_e to count the letter "o" instead.
# Predict average_of_list for [4, 8, 6]. Then try [10] and [2.5, 3.5].


# PRACTICE C: A while loop repeats while its condition is True
# A for loop knows how many passes it will make. A while loop keeps going
# until its condition becomes False, so YOU must change a variable inside it.
# Trace table (complete it BEFORE running with start = 3):
#   check | count | count > 0 ? | action
#   ------+-------+-------------+------------------
#     1   |   3   |   True      | add 3, then count becomes 2
#     2   |   2   |   ?         | ?
#   (continue until the condition is False)
def sum_with_while_loop(start):
    """Return the sum of start + (start-1) + ... + 1."""
    total = 0
    count = start
    while count > 0:
        total = total + count
        count = count - 1
    return total


# Breakpoint practice: put a breakpoint on "while count > 0:". Step through.
# Tinker: call it with 0. Does the loop body ever run? Why not?


# PRACTICE D: While loops for "until we reach a goal"
# We do not know the number of passes ahead of time, so while is a good fit.
# Predict: how many years until 1000 grows past 2000 at 7% per year?
def years_to_double(amount, rate):
    """Return the number of years needed for amount to double."""
    goal = amount * 2
    years = 0
    while amount < goal:
        amount = amount * (1 + rate)
        years = years + 1
    return years


# Tinker: try rates of 0.10 and 0.02. Predict whether years go up or down.


# PRACTICE E: for or while?
# Both functions below produce the same answer. Trace each one with n = 4.
def factorial_for(n):
    """Return n factorial computed using a for loop."""
    result = 1
    for factor in range(1, n + 1):
        result = result * factor
    return result


def factorial_while(n):
    """Return n factorial computed using a while loop."""
    result = 1
    factor = 1
    while factor <= n:
        result = result * factor
        factor = factor + 1
    return result


# Explain in a comment: which one needs us to create and update our own
# counter variable? Which one is easier to read for a fixed number of passes?


# PRACTICE F: More debugging
# Predict what is wrong, then use a breakpoint to confirm it.
#
# F1. Off-by-one: it should add 1 through 5 (answer 15).
def sum_to_five_buggy():
    """Return the sum of 1 through 5 (contains a bug)."""
    total = 0
    for number in range(1, 5):
        total = total + number
    return total


# F2. Infinite loop: this should count down from start to zero and return
# the number of passes (3 for start = 3). It is NOT called in main() because
# it never ends as written. Find the missing line and fix it, then add the
# call to main(). (Stop a runaway program with Ctrl+C in the terminal.)
def countdown_buggy(start):
    """Return the number of passes made counting down to zero (has a bug)."""
    count = start
    passes = 0
    while count > 0:
        passes = passes + 1
    return passes


# PRACTICE G: Write your own loops
# Complete these two functions. Use a breakpoint if the result is surprising.
def sum_of_evens(limit):
    """Return the sum of the even numbers from 2 up to limit.

    For limit = 10 the sum is 2 + 4 + 6 + 8 + 10 = 30.
    Hint: range(2, limit + 1, 2) counts by twos.
    """
    total = 0
    # TODO: write a for loop that adds each even number to total.
    return total


def count_doublings(start, limit):
    """Return how many times start can be doubled until it is above limit.

    For start = 3 and limit = 50: 3 -> 6 -> 12 -> 24 -> 48 -> 96, so 5 doublings.
    Hint: use a while loop and a counter.
    """
    doublings = 0
    # TODO: write a while loop that doubles start and counts each doubling.
    return doublings


def main():
    """Call each function with simple test cases."""
    print("PART 1")
    print("1. Sum of odds 1-6:", sum_of_odds_to_six())
    print("2. Sum of multiples of 3 up to 10:", sum_of_multiples_of_three(10))
    print("3. run pytest to run unit test test_count_above() in test_tinkering_with_loops.py")
    print("4. Total of list:", total_list_buggy([3, 4, 5]))

    print()
    print("PART 2: MORE PRACTICE")
    print("A. Sum of 1 to 4:", sum_with_for_loop())
    print("B. Letter e count:", count_letter_e("beer"))
    print("B. Average:", average_of_list([4, 8, 6]))
    print("C. Sum counting down from 3:", sum_with_while_loop(3))
    print("D. Years to double:", years_to_double(1000, 0.07))
    print("E. 4! with for:", factorial_for(4))
    print("E. 4! with while:", factorial_while(4))
    print("F1. Sum of 1 to 5:", sum_to_five_buggy())
    # F2: add print("F2. Countdown passes:", countdown_buggy(3)) after
    # you fix the function.
    print("G. Sum of evens to 10:", sum_of_evens(10))
    print("G. Doublings of 3 above 50:", count_doublings(3, 50))

    # CHECK-OUT QUESTIONS
    # 1. What are the first and last values produced by range(2, 7)?
    # 2. When is a while loop a better choice than a for loop?
    # 3. What causes an infinite loop?
    # 4. What did the breakpoint show you that a print statement would not?


if __name__ == "__main__":
    main()
