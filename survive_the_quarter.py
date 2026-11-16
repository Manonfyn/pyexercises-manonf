# Manon Fayon - Groupe CL10

# 1. What goes in?
# The file scenarios_C.csv uses commas to separate its 14 columns.
# Each row has a situation, its number, three choices, three reputation
# changes, three budget changes, and three feedback messages.
# The changes have a sign and a unit, like +15 pts or -800 EUR.

# 2. What happens?
# Show the day number, the budget, and the reputation.
# Show the situation and the choices A, B, and C.
# Ask for a choice and ask again if it is invalid.
# Apply the choice to the budget and reputation.
# Keep reputation at 100 if it goes above 100.
# Show the feedback message and record the move.
# Stop the game if the budget or reputation is zero or less.

# 3. What comes out?
# The player sees why they were fired, or their final score and title.
# The game also shows the best and worst moves based on reputation changes.
# Each line in results.csv saves the player's name, final budget,
# final reputation, title, and date, in that order.

# 4. What could go wrong?
# Invalid choice: ask again until the player types A, B, or C.
# Budget or reputation at zero or less: stop and explain why the player was fired.
# Missing CSV file: show an error message and stop before starting the game.

# I chose option D: Difficulty.
# I chose it because the player can decide how challenging the game will be.


import csv


# Read the scenarios and store the three choices for each situation.
def load_scenarios():
    scenarios = []

    with open("scenarios_C.csv", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            choices = []

            for number in range(1, 4):
                text = row[f"Decision {number}"]
                budget_change = int(row[f"Budget {number}"].split()[0])
                reputation_change = int(row[f"Reputation {number}"].split()[0])
                feedback = row[f"Outcome {number}"]

                choices.append((text, budget_change, reputation_change, feedback))

            scenarios.append({"event": row["Event"], "choices": choices})

    return scenarios



# Ask for a choice until the player enters A, B, or C.
def ask_choice():
    choice = input("Your choice (A, B or C): ").strip().upper()

    while choice not in ("A", "B", "C"):
        choice = input("Please type A, B or C: ").strip().upper()

    return choice


# Update the budget and reputation after a choice.
def apply_choice(budget, reputation, budget_change, reputation_change):
    budget = budget + budget_change
    reputation = reputation + reputation_change

    if reputation > 100:
        reputation = 100

    return budget, reputation


    # Ask for the difficulty and return the starting budget.
def choose_budget():
    difficulty = input("Choose a difficulty (easy or hard): ").strip().lower()

    while difficulty not in ("easy", "hard"):
        difficulty = input("Please type easy or hard: ").strip().lower()

    if difficulty == "easy":
        return 15000

    return 6000

    # Show one situation and apply the player's choice.
def play_day(day, scenario, budget, reputation):
    print(f"\n--- Day {day} ---")
    print(f"[Budget: {budget} EUR | Reputation: {reputation}/100]")
    print(scenario["event"])

    choices = scenario["choices"]
    for index, letter in enumerate("ABC"):
        print(f"  {letter}: {choices[index][0]}")

    letter = ask_choice()
    index = "ABC".index(letter)
    text, budget_change, reputation_change, feedback = choices[index]

    old_reputation = reputation
    budget, reputation = apply_choice(
        budget, reputation, budget_change, reputation_change
    )

    actual_change = reputation - old_reputation
    print(feedback)
    print(f"Budget {budget_change:+d} EUR, Reputation {actual_change:+d}")

    move = (actual_change, day, text)
    return budget, reputation, move


# Shuffle the scenarios and play up to ten days.
def play_game(scenarios, budget):
    import random

    random.shuffle(scenarios)
    reputation = 50
    history = []

    for day, scenario in enumerate(scenarios[:10], start=1):
        budget, reputation, move = play_day(day, scenario, budget, reputation)
        history.append(move)

        if budget <= 0 or reputation <= 0:
            break

    return budget, reputation, history

# Show the final result and return the player's title.
def show_result(name, budget, reputation):
    if budget <= 0 or reputation <= 0:
        print(f"{name}, you were fired!")
        if budget <= 0:
            print("You ran out of budget.")
        if reputation <= 0:
            print("Your reputation dropped to zero or below.")
        return "Fired"

    score = reputation + budget // 200

    if score < 95:
        title = "Eternal Intern"
    elif score < 120:
        title = "Growth Hacker"
    elif score < 140:
        title = "CMO Material"
    else:
        title = "Viral Legend"

    print("\nQuarter survived!")
    print(f"Budget left: {budget} EUR, reputation: {reputation}/100")
    print(f"Final score: {score}")
    print(f"{name}, your title: {title}")
    return title

    # Show the moves with the highest and lowest reputation changes.
def show_moves(history):
    best_change, best_day, best_text = max(history)
    worst_change, worst_day, worst_text = min(history)

    print(f'Best move: day {best_day}, "{best_text}" ({best_change:+d})')
    print(f'Worst move: day {worst_day}, "{worst_text}" ({worst_change:+d})')

    # Save one line for each completed game.
def save_result(name, budget, reputation, title):
    from datetime import date

    with open("results.csv", "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow((name, budget, reputation, title, date.today().isoformat()))

    print("Saved in results.csv")


    # Run the game from start to finish.
def main():
    name = input("What is your name? ").strip()

    try:
        scenarios = load_scenarios()
    except FileNotFoundError:
        print("Cannot find scenarios_C.csv.")
        return

    budget = choose_budget()
    budget, reputation, history = play_game(scenarios, budget)
    title = show_result(name, budget, reputation)
    show_moves(history)
    save_result(name, budget, reputation, title)


if __name__ == "__main__":
    main()