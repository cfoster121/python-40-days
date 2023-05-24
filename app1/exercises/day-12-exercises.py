# EXERCISE 1
# create fx converting liters to m^3

liters = input("enter liters: ")


def conv_liters(liters):
    liters_val = liters.strip(" ")
    liters_int = float(liters_val)

    meters_cube = liters_int / 1000

    return meters_cube

conv_liters(liters)


# EXERCISE 2
# ask user for password, create fx checking strength if ALL are true:
# 8+ chars, 1+ uppercase, 1+ digit
# print strong password or weak password

password = input("enter new password: ")

def pass_strength(password):

    result = {}

    if len(password) > 7:
        result["length"] = True
    else:
        result["length"] = False

    result["cap"] = False
    result["num"] = False

    for char in password:
        if char.isupper():
            result["cap"] = True
        if char.isdigit():
            result["num"] = True

    if all(result.values()):
        return("strong password")
    else:
        return("weak password")

print(pass_strength(password))

