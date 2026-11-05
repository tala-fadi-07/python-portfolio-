# fix_the_stats.py
# Count failed logins and the average session length 
events = ["FAILED", "SUCCESS", "FAILED", "SUCCESS", "SUCCESS"]
minutes = [0, 30, 0, 15, 45]

# Bug 1:* failed was set to 0 INSIDE the loop, so it reset every time *
# Fix: set the counter to 0 BEFORE the loop starts.
failed = 0
for event in events:
    if event == "FAILED":
        failed += 1
print(f"Failed logins: {failed}")

total = 0
count = 0
for value in minutes:
    if value > 0:
        total += value
        count += 1

# Bug 3: print was INSIDE the loop, so it printed 3 times.
# Fix: move it OUTSIDE the loop, after counting is done.
# Bug 2: // is integer division and gives 30, / gives 30.0
# Fix: use / instead of //
print(f"Average session: {total / count} minutes.")

# Bug 4: range(1, 4) stops at 3, it never reaches 4.
# Fix: use range(1, 5) to include 4.
for level in range(1, 5):
    print(f"Level {level}")