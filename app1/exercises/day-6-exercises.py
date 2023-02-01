# EXERCISE 1: Create a program that reads essay.txt and prints text with first letter of each word capitalized

file = open("../files/essay.txt", 'r')
content = file.read()
print(content.title())


# EXERCISE 2: Read essay.txt and return number of characters in file

file = open("../files/essay.txt", 'r')
content = file.read()
length = len(content)
print(length)


# EXERCISE 3: Create program prompting user to enter new member to list, add to members.txt

newMem = input("Please enter new member name: ")

file = open("../files/members.txt", 'r')
members = file.readlines()
file.close()

members.append(newMem + '\n')

file = open("../files/members.txt", 'w')
file.writelines(members)
file.close()


# EXERCISE 4: Iterate over filenames list, create new files with content 'Hello'

filenames = ['new1.txt', 'new2.txt', 'new3.txt']

for filename in filenames:
    file = open(f"../files/{filename}", 'w')
    file.write("Hello")
    file.close()


# EXERCISE 5: Print content from a.txt, b.txt, c.txt to console

files = ['a', 'b', 'c']

for file in files:
    content = open(f"../files/{file}.txt", 'r')
    print(content.read())