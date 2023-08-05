""" Implement a program that reads user input for a password. Create a custom
exception WeakPasswordError to handle cases where the password is shorter
than 8 characters. """

class WeakPasswordError(Exception):
    pass

def check_password(password):
    if len(password) < 8:
        raise WeakPasswordError("Password should be atleast 8 characters long")

try:
    password = input("Enter your password: ")
    check_password(password)
except WeakPasswordError as e:
    print("Error: ",e)
