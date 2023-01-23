# EXERCISE 1: Prompt user to input a (dollar) amount, Calculate the corresponding amount in euros, given an exchange rate of 0.95, Print out the amount in euros

dollars = input("USD amount: $")
euros = int(dollars) * 0.95
print("€", euros)


# EXERCISE 2: Take list, prompt user for rank number (list index), return name at rank

names = ['Adam', 'Bob', 'Chris', 'Dave', "Eddie"]

print(names)
name = input("Which ranking would you like to see? ")
print(names[int(name)])


# EXERCISE 3: Take list, prompt user for name, return rank number (list index)

names = ['Adam', 'Bob', 'Chris', 'Dave', "Eddie"]

print(names)
rank = input("Whose rank would you like to see? ")
index = names.index(rank) + 1
print(index)