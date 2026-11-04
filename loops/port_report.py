# port.report.py
# Aport report 
start = int(input("Start port: "))
end = int(input("End port: "))

count = 0

for port in range(start, end + 1):
    if port <= 1023:
        category = "system"
    elif port <= 49151:
        category = "user"
    else:
        category = "dynamic"

    print(f"{port}: {category}")
    count += 1

print(f"Ports checked: {count}")