# password.py
# brenden west
# 10-30-2016

# get password from user
# check length >= 8 and <= 80
# check if has number
# check if has a lower case char
# check if has an upper case char

def main():
    password = input("Password: ")
    
    if len(password) < 8 or len(password) > 80:    # validate length
        print("password must be between 8 and 80 characters")
    elif password.isalpha(): # validate has a number
        print("Password must contain a number")
    elif password.isdigit(): # validate has letters
        print("Password must contain letters")
    elif password.isupper() or password.islower():    # validate has both upper & lower case
        print("Password must contain upper-case and lower-case letters")
    else:
        print("valid")

main()