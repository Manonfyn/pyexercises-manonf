"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: 8 campaigns budgets
# 2. Process, function by function: calculate_total() adds the budgets.
#   find_highest_budget() finds the largest budget.
#    calculate_percentage() calculates its share of the total.
#    highest_budget_share() calls these three functions in order.
# 3. Out:The largest budget represents 22.22% of the total.
# 4. The question my fourth function answers: What percentage of the total is the largest budget?
# Splitting the work lets me test each step separately.


# Your code below
def calculate_total(budgets):
    return sum(budgets)


def find_highest_budget(budgets):
    return max(budgets)


def calculate_percentage(amount, total):
    return amount / total * 100


def highest_budget_share(budgets):
    total = calculate_total(budgets)
    highest = find_highest_budget(budgets)
    return calculate_percentage(highest, total)


# Input: [100, 200]. Expected: 300.
print("Total test:", calculate_total([100, 200]))

# Input: [100, 200]. Expected: 200.
print("Highest budget test:", find_highest_budget([100, 200]))

# Inputs: 50 and 200. Expected: 25.0.
print("Percentage test:", calculate_percentage(50, 200))

budgets = [100, 200, 150, 300, 250, 400, 350, 500]
share = highest_budget_share(budgets)

print("The highest budget represents", round(share, 2), "% of the total.")