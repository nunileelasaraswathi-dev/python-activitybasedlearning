level = int(input("Initial water level: "))
capacity = int(input("Tank capacity: "))
threshold = int(input("Target level: "))

for day in range(1, 8):
    inflow = int(input("Inflow: "))
    outflow = int(input("Outflow: "))
    level += inflow - outflow

    if level > capacity:
        print("Overflow:", level - capacity)
        level = capacity
    if level < 0:
        print("Shortage:", -level)
        level = 0

    print("Day", day, "Water:", level)
    if level >= threshold:
        print("Threshold reached on day", day)
        break