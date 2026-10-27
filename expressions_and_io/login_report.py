#login_report.py 
MAX_LOGIN_ATTEMPTS = 5
username = input("Username: ")
failed = int(input("Failed attempts: "))

left = MAX_LOGIN_ATTEMPTS - failed

print("=" * 30)
print("LOGIN REPORT")
print("=" * 30)
print(f"User:\t\t{username}")
print(f"Failed:\t\t{failed}")
print(f"Attempts left:\t{left}")