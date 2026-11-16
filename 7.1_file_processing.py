"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - Some lines are empty.
# - Some lines start with extra spaces.
# - Capital letters are inconsistent.
# - One last name has two words: van rossum.

# 1. In: The lines in names.txt.
# 2. Process, problem by problem: 
# - Skip empty lines.
# - Remove spaces at the start and end of each line.
# - Capitalize the first letter of each word.
# - Keep all words after the first name together, then sort by last name.
# 3. Out: A new file, clean_names.txt, with the cleaned and sorted names
# 4. How I decide which word is the last name: The first word is the first name. Everything after it is the last name.
# For example, in "Guido Van Rossum", the last name is "Van Rossum".


# Your code below

def last_name(full_name):
    return full_name.split(" ", 1)[1].lower()


names = []

with open("names.txt", "r", encoding="utf-8") as file:
    for line in file:
        clean_name = line.strip()
        if clean_name:
            names.append(clean_name.title())

names.sort(key=last_name)

with open("clean_names.txt", "w", encoding="utf-8") as file:
    for name in names:
        file.write(name + "\n")

print("Clean names saved in clean_names.txt.")
