# ip_check.py
# checked ipv4 
def is_valid_part(part):
    if not part.isdecimal():
        return False
    if int(part) > 255:
        return False
    return True

def ip_problem(address):
    if address.count(".") != 3:
        return "it needs exactly 3 dots."

    parts = address.split(".")

    for part in parts:
        if part == "":
            return "a part is empty."
        if not is_valid_part(part):
            return f"{part} is not a number from 0 to 255."

    return ""

address = input("IPv4 address: ").strip()
problem = ip_problem(address)

if problem == "":
    print(f"{address} is valid.")
else:
    print(f"Invalid: {problem}")