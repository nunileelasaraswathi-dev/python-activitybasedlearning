n = int(input("Enter number of subjects: "))
marks = []

for i in range(n):
    m = int(input(f"Enter marks for subject {i+1}: "))
    if m < 0 or m > 100:
        print("Invalid marks")
        exit()
    if 30 <= m < 35:
        m = min(m + 5, 100)
    marks.append(m)

total = sum(marks)
percentage = total / n

print("Final Marks:", marks)
print("Total:", total)
print("Percentage:", round(percentage, 2), "%")

if any(m < 35 for m in marks):
    print("Result: FAIL")
elif percentage >= 75:
    print("Result: DISTINCTION")
elif percentage >= 60:
    print("Result: FIRST CLASS")
elif percentage >= 50:
    print("Result: SECOND CLASS")
else:
    print("Result: PASS")