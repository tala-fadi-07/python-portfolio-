# username_policy.py
# policy the username
MIN_LENGTH = 3
MAX_LENGTH = 12

def clean(username):
    return username.strip().lower()

def bad_character(username):
    for ch in username:
        if not (ch.isalpha() or ch.isdigit() or ch == "_"):
            return ch
    return ""

def policy_problem(username):
    if not (MIN_LENGTH <= len(username) <= MAX_LENGTH):
        return "length must be 3 to 12."
    if not username[0].isalpha():
        return "it must start with a letter."
    bad = bad_character(username)
    if bad != "":
        return f"the character {bad} is not allowed."
    return ""

username = input("New username: ")
cleaned = clean(username)
problem = policy_problem(cleaned)

if problem == "":
    print(f"Accepted [{cleaned}].")
else:
    print(f"Rejected [{cleaned}]: {problem}")