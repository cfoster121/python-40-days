# EXERCISE 1
# create fx with params year_of_birth and current_year, current_year defaulted to 2023
# fx calculates and returns age of user

def find_age(year_of_birth, current_year = 2023):
    age = current_year - year_of_birth
    return age

# EXERCISE 2
# use fx from exercise 1, prompt for input, print age

def find_age(year_of_birth, current_year = 2023):
    age = current_year - year_of_birth
    return age

birth_year = int(input("please enter the year you were born: "))
age = find_age(birth_year)
print(age)

# EXERCISE 3
# return message if age>120

def find_age(year_of_birth, current_year = 2023):
    age = current_year - year_of_birth
    return age

birth_year = int(input("please enter the year you were born: "))
age = find_age(birth_year)
if (age >= 120):
    print(f"if you are {age}, you are too old")
else:
    print(age)

# EXERCISE 4
# write fx taking list of names returning number of names

def num_names(input):
    name_list = input.split(",")
    return len(name_list)

names = input("enter names separated by commas, no spaces: ")
list_len = num_names(names)
print(list_len)