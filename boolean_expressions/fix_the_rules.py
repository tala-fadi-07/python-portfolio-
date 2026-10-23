# fix_the_rules.py
# This program checks a connection against three rules.

role = input("Role: ")
# runtime: input gives string, must convert to int for numeric compare
port = int(input("Port: "))
# semantic: was = (assignment) which overwrites role, need == (comparison)
is_admin = role == "admin"
# syntax: =< is invalid operator, correct is <=
is_system_port = port <= 1023
# semantic: or 443 is always True, must compare port on both sides
is_web_port = port == 80 or port == 443
print(f"Admin: {is_admin}")
print(f"System port: {is_system_port}")
print(f"Web port: {is_web_port}")