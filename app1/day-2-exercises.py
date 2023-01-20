# EXERCISE 1: Prompt user to enter name once, print name with first letter capitalized

name = input("Enter your name: ")
print(name.capitalize())


# EXERCISE 2: Create a program that prompts the user to input their name once. Then, the program repeatedly prints out the name with the first letter capitalized

user_prompt = name = input("Enter your name: ")

while True:
    print(name.capitalize())


# EXERCISE 3: Create a program that prompts the user to input their name repeatedly. Then, the program repeatedly prints out the name with the first letter capitalized.

while True:
    name = input("Enter your name: ")
    print(name.capitalize())
