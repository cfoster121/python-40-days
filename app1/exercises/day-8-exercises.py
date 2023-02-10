# Create program that asks user to input heads or tails after throwing coin, calculates % of heads thrown, creates new file storing each throw on new line
#
# PSUEDOCODE:
# Create head, tails, and total counters starting at 0
# Ask user to flip coin
# Ask user to input 'heads' or 'tails'
# Add input to .txt file
# add 1 to head or tail counter
# add 1 to total counter
# calculate % of heads
# print % of heads
# repeat

heads = 0
tails = 0
total = 0
percent = 0
file = open('../files/headtails.txt', 'w')

while True:

    throw = input("Throw coin and enter H or T: ")
    throw = throw.capitalize()

    if throw == 'H':
        heads = heads + 1
        total = total + 1
        percent = heads/total

        with open('../files/headtails.txt', 'a') as file:
            file.write(f"Heads\n")

        print(f"Heads: {heads}\nTails: {tails}\nTotal Throws: {total}\n% of Heads: {percent}")

    if throw == 'T':
        tails = tails + 1
        total = total + 1
        percent = heads/total

        with open('../files/headtails.txt', 'a') as file:
            file.write(f"Tails\n")

        print(f"Heads: {heads}\nTails: {tails}\nTotal Throws: {total}\n% of Heads: {percent}")

    else:
        print('Please enter H or T')