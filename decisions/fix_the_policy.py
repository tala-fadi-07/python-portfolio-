# fix_the_policy.py
# check a new password against an example policy and classify its length
MIN_LENGTH = 12

username = input("username: ")
password = input("New password: ")

if len(password) < MIN_LENGTH:  # FIX 1: syntax 
    print("- Too short.")
if password == username:  # FIX 2: semantic 
    print("- Same as the username.")
if len(password) >= 16:  # FIX 3: semantic 
    strength = "long"
elif len(password) >= MIN_LENGTH:
    strength = "acceptable"
else:
    strength = "short"

print(f"Length: {len(password)} ({strength})")  # FIX 4: semantic 