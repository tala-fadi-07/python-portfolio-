# fix_the_record.py
# This program prints a short record about a network device.

device_name = "edge-router"
# syntax error - variable name cannot start with a number
second_ip = "192.0.2.1"
# syntax error - 'class' is a reserved keyword
device_class = "router"
# runtime error - cannot convert non-numeric string to int
port = 22
# runtime error - NameError due to typo device_nam
print("Device:", device_name)
# syntax error - same invalid variable name 2nd_ip
print("Backup IP:", second_ip)
print("Type:", device_class)
print("Port:", port)

# Python reports syntax errors first because it parses the whole file before executing
# The syntax errors (2nd_ip and class) are caught during parsing, while runtime errors
# (int("twenty-two") and device_nam) only appear after syntax is correct and code starts running.