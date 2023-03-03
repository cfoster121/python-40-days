# Create program to check password strength, if >7 characters print strong password, if <=7 characters print weak password
# if == 7 characters print password ok but not strong


password = input("Please enter a password: ")

if len(password) < 7:
    print("Weak password")
elif len(password) == 7:
    print("Password ok, not strong")
else:
    print("Strong password")

