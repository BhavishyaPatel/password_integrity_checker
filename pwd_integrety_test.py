import string

def pwd_strength(pwd: str):
    
    points = 0
    space = 0
    yes_upper = yes_lower = yes_digit = yes_special = yes_space = False
    no_upper = no_lower = no_digit = no_special = True

    for ch in pwd:
        if ch==" ":
            yes_space = True
        if ch.isupper():
            yes_upper = True
            no_upper = False
        if ch.islower():
            yes_lower = True
            no_lower = False
        if ch.isdigit():
            yes_digit = True
            no_digit = False
        if ch in string.punctuation:
            yes_special = True
            no_special = False

    if yes_upper:
        points += 1
    if yes_lower:
        points += 1
    if yes_digit:
        points += 1
    if yes_special:
        points += 1
    if len(pwd) >= 8:
        points += 1
    if yes_space:
        space += 1
    
    missing = []
    if no_upper:
        missing.append("an uppercase letter")
    if no_lower:
        missing.append("a lowercase letter")
    if no_digit:
        missing.append("a digit")
    if no_special:
        missing.append("a special character")
    if len(pwd) < 8:
        missing.append("number of characters (should have 8 characters minimum)")

    return points, missing, space

def check_pwd(pwd: str):
    
    points, missing, space = pwd_strength(pwd)
    
    if points == 0:
        if space == 1:
            print("Password is too weak, also try using underscore ( _ ) instead of spaces")
        else:
            print("Password is too weak.")
    elif points == 1:
        if space == 1:
            print("Password is very weak, also try using underscore ( _ ) instead of spaces")
        else:
            print("Password is very weak.")
    elif points == 2:
        if space == 1:
            print("Password is weak, also try using underscore ( _ ) instead of spaces")
        else:
            print("Password is weak.")
    elif points == 3:
        if space == 1:
            print("Password is moderate, also try using underscore ( _ ) instead of spaces")
        else:
            print("Password is moderate.")
    elif points == 4:
        if space == 1:
            print("Password is strong, but try using underscore ( _ ) instead of spaces")
        else:
            print("Password is strong.")
    elif points == 5:
        if space == 1:
            print("Password is very strong, but it is suggested to add underscore( _ ) instead of spaces")
        else:
            print("Password is very strong.")

    if missing:
        print("Make sure to add these: " + ", ".join(missing))
print("\n********** WELCOME TO PASSWORD INTEGRETY CHECK **********\n")
print("Enter your password below to check its integrety (enter 0 to terminate the program).")

while True:
    pwd = input("\nPassword: ")
    
    if pwd == "0":
        print("\n********** Thank you! **********\n")
        break
    else:
        check_pwd(pwd)
