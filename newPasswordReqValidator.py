# This program asks the user to input
# a password requiring:
# >= 8 characters,
# has at least 1 uppercase & 1 lowercase letter,
# & has at least one digit.
# It then evaluates the input and
# tells the user whether or not it is valid.


print("Please create a new password that: ")
print("• is at least 8 characters long ")
print("• must have at least one uppercase and one lowercase character ")
print("• & must have at least one digit. ")
print(" ")


# Declare password validator function.
def passwordValid(password):
    # Checks if password meets required conditions; false = no, true = yes:
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    else:
        return True

# Declare function that prompts user for password,
# confirms it, & responds to invalid inputs.
def getPassword():
    # Prompt user to input and confirm a password.
    while True:
        print(" ")
        password = input("Enter a new password: ")
        confirmPassword = input("Confirm password: ")
        # Verify passwords match.
        if password != confirmPassword:
            print("Error: Passwords do not match. ")
            continue
           # Catch invalid password. 
        if not passwordValid(password):
            print("Error: Password invalid. Verify password requirements are met. ")
            continue
        return password


# Declare main function that outputs once valid password entry is successful.
def main():
    password = getPassword()
    print(" ")
    print("Success: Password is valid. ")


# Call main to execute.
main()

        
