# risk_score.py 

score = 0

failed = int(input("Failed attempts in the last hour: "))
hour = int(input("Login hour (0-23): "))
new_device = input("New device (yes/no): ").lower()

# Rule 1: 3 or more failed attempts = +40
if failed >= 3:
    score += 40

# Rule 2: login before 6 AM = +30
if hour < 6:
    score += 30

# Rule 3: new device yes = +30
if new_device == "yes":
    score += 30

# Classify - THINK: which is separate if and which is chain?
if score >= 70:
    level = "HIGH"
elif score >= 30:
    level = "MEDIUM"
else:
    level = "LOW"

print(f"Risk score: {score} ({level})")