subjects = int(input("Number of subjects: "))
old, new = [], []

for i in range(subjects):
    old.append(int(input("Previous score: ")))
    new.append(int(input("Current score: ")))

for i in range(subjects):
    print("Subject", i+1, "Change:", new[i] - old[i])

weak = [i+1 for i in range(subjects) if new[i] < 35]
print("Weak subjects:", weak)

avg = sum(new) / subjects
print("Average:", avg)
print("Result:", "Pass" if not weak else "Fail")