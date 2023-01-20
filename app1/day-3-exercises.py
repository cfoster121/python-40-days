# EXERCISE 1:
# Create a program that does the following:
# 1. Prompts the user to input the country they are from.
# 2. If the user enters the word USA, the program prints out Hello.
# 3. If the user enters the word  India, the program prints out Namaste.
# 4. If the user enters the word Germany, the program prints out Hallo.

while True:

    user_prompt = input("Enter 'USA', 'India', or 'Germany' to learn how to say Hello! ")
    user_prompt = user_prompt.capitalize()

    match(user_prompt):
            case('USA' | 'Usa'):
                print('Hello')
            case('India'):
                print('Namaste')
            case('Germany'):
                print('Hallo')
            case _:
                print("Please enter 'USA', 'India', or 'Germany'")


# EXERCISE 2 : Use for loop to print individual, capitalized names from array

names = ["john smith", "sen plakay", "dora ngacely"]

for name in names:
    name = name.title()
    print(name)
