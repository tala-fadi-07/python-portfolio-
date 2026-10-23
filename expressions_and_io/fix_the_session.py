# fix_the_session.py
# This program reports a user's session time.
username = input("Username: ")

# Fix 1: runtime * input returns string, need int for math*
total_seconds = int(input("Session length in seconds: "))
# Fix 2: semantic * need floor division // to get whole minutes*
minutes = total_seconds // 60
seconds = total_seconds % 60

print("=" * 30)
# Fix 3: semantic - missing f for f-string, was printing literal {username}
print(f"User: {username}")
# Fix 4: runtime - minutes is int can't concat with string, need str() or f-string
print(f"Session: {minutes} min {seconds} s")
print("=" * 30)