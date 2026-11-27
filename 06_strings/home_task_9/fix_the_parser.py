# fix_the_parser.py
# debuging
# fix_the_parser.py
LINE = "09:02 FAILED user=Admin ip=192.0.2.7"

def get_time(line):
    """Return the time: the first 5 characters."""
    # semantic: time is 5 chars "09:02", not 4
    return line[0:5]

def get_user(line):
    """Return the user name in lowercase."""
    start = line.find("user=") + 5
    end = line.find(" ", start)
    user = line[start:end]
    # semantic: lower() returns a new string; keep it
    user = user.lower()
    return user

def is_failed(line):
    """Return True if the line reports a failed login"""
    # semantic: LINE has "FAILED" uppercase, not "failed"
    return "FAILED" in line

def hide_first(user):
    """Return user with its first letter replaced by "*"."""
    # runtime: strings are immutable, cannot do user[0] = "*"
    return "*" + user[1:]

print(f"Time: {get_time(LINE)}")
print(f"User: {get_user(LINE)}")
print(f"Failed: {is_failed(LINE)}")
print(f"Hidden: {hide_first('admin')}")
# runtime: len() is a function, not a method LINE.len()
print(f"Length: {len(LINE)}")