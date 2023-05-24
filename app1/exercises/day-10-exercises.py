# EXERCISE 1
# Build a percentage calculator that gets from the user the "total value" and the "value" and returns the percentage
# print message if user does not enter number for total value or value

# EXERCISE 2
# print error message if total value is 0

try:
    total = float(input("enter total value: "))
    value = float(input("enter percent value: "))

    percent = 'that is ' + str((value/total * 100)) + '%'
    print(percent)
except ValueError:
    exit("please enter a number")
except ZeroDivisionError:
    exit("total value cannot be 0")
