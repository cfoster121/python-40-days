# EXERCISE 1: Capitalize names in list and return new values

names = ["john smith", "jay santi", "eva kuki"]

names = [name.title() for name in names]
print(names)


# EXERCISE 2: Print number of characters in each username

usernames = ["john 1990", "alberta1970", "magnola2000"]

usernames = [len(user) for user in usernames]
print(usernames)


# EXERCISE 3: Reprint list as floats

user_entries = ['10', '19.1', '20']

user_entries = [float(entry) for entry in user_entries]
print(user_entries)


# EXERCISE 4: Print sum of values

user_entries = ['10', '19.1', '20']

nums = [float(entry) for entry in user_entries]
print(sum(nums))