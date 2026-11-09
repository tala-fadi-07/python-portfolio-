# password_check.py
# This file checks if a password is long enough and different from username.
def long_enough(password, minimum=8):
    return len(password) >= minimum

def differs_from_username(password, username):
    return password != username

def password_ok(password, username):
    return long_enough(password) and differs_from_username(password, username)

username = input("Username: ")
password = input("Password: ")

if password_ok(password, username):
    print("Password accepted.")
else:
    print("Password rejected.")