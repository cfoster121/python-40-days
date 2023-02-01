# EXERCISE 1: Print list as index-Item.txt

filenames = ['document', 'report', 'presentation']

for index, item in enumerate(filenames):
    print(f"{index}-{item.capitalize()}.txt")


# EXERCISE 2: For list of IP addresses, ask user to input index, return corresponding IP address

ips = ['100.122.133.105', '100.122.133.111']

user_action = int(input("Enter 0 or 1: "))
print(f"IP address: {ips[user_action]}")
