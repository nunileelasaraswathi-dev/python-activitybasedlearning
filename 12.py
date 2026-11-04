attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes: "))
threshold = float(input("Enter eligibility percentage: "))

percentage = attended / total * 100
print("Current Attendance:", round(percentage, 2), "%")

if percentage >= threshold:
    print("Already Eligible")
else:
    needed = 0
    while (attended + needed) / (total + needed) * 100 < threshold:
        needed += 1
    print("Consecutive classes required:", needed)
    print("Attendance after recovery:",
          round((attended + needed) / (total + needed) * 100, 2), "%")