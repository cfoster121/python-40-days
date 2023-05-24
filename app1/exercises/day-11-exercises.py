# EXERCISE 1
# calculate/print max value of grades list
# EXERCISE 2
# return min and max values

def get_max():
    grades = [9.6, 9.2, 9.7]
    max_local = max(grades)
    min_local = min(grades)
    message = f'Max: {max_local}, Min: {min_local}'
    return message

print(get_max())


# BUG FIXING
def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    return maximum


celsius = get_maximum()

fahrenheit = celsius * 1.8 + 32
print(fahrenheit)