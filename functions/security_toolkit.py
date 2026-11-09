# security_toolkit.py
# This file is a security toolkit with a menu for port, password and PIN checks.

MIN_LENGTH = 8

def border(width):
    """Print a border line."""
    print("+" + "-" * (width + 2) + "+")

def show_box(text):
    """Print text inside a box."""
    border(len(text))
    print("| " + text + " |")
    border(len(text))

def show_menu():
    """Print the main menu."""
    print("SECURITY TOOLKIT")
    print("1. Check a port")
    print("2. Check a password")
    print("3. PIN guessing time")
    print("q. Quit")

def check_port(port):
    """Return the range of a port."""
    if port < 0 or port > 65535:
        return "invalid"
    if port <= 1023:
        return "system"
    if port <= 49151:
        return "user"
    return "dynamic"

def port_range():
    """Ask for a port and show its range in a box."""
    port = int(input("Port: "))
    result = check_port(port)
    show_box(f"Port {port}: {result}")

def password_problem(password, username):
    """Return the first password problem, or empty string."""
    if len(password) < MIN_LENGTH:
        return "too short (at least 8)"
    if password == username:
        return "same as the username"
    return ""

def check_password():
    """Ask for username and password and show accepted or rejected."""
    username = input("Username: ")
    password = input("Password: ")
    problem = password_problem(password, username)
    if problem == "":
        show_box("Password accepted")
    else:
        show_box(f"Rejected: {problem}")

def days_to_guess(digits, per_second):
    """Return whole days to try every PIN."""
    return 10 ** digits // per_second // 86400

def check_pin():
    """Ask for PIN digits and show days to guess in a box."""
    digits = int(input("PIN digits: "))
    per_second = int(input("Guesses per second: "))
    days = days_to_guess(digits, per_second)
    show_box(f"{digits} digits: {days} days")

show_menu()
checks = 0

while True:
    choice = input("Choice (1, 2, 3, or q): ")
    if choice == "q":
        break
    elif choice == "1":
        port_range()
        checks = checks + 1
    elif choice == "2":
        check_password()
        checks = checks + 1
    elif choice == "3":
        check_pin()
        checks = checks + 1
    else:
        print("Unknown choice.")

show_box(f"Checks done: {checks}")