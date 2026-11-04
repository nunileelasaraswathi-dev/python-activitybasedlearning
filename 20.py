n = int(input("Number of candidates: "))
candidates = []

for i in range(n):
    name = input("Candidate name: ")
    math = int(input("Math marks: "))
    science = int(input("Science marks: "))
    total = int(input("Aggregate marks: "))

    if math >= 35 and science >= 35 and total >= 75:
        candidates.append((name, total))

candidates.sort(key=lambda x: -x[1])

print("Admission Ranking:")
for rank, (name, marks) in enumerate(candidates, 1):
    print(rank, name, marks)