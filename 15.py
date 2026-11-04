from datetime import datetime

entry = input("Entry (YYYY-MM-DD HH:MM): ")
exit = input("Exit (YYYY-MM-DD HH:MM): ")

try:
    e = datetime.strptime(entry, "%Y-%m-%d %H:%M")
    x = datetime.strptime(exit, "%Y-%m-%d %H:%M")
    if x <= e:
        print("Invalid time")
    else:
        hours = (x-e).total_seconds() / 3600
        rate = {"car": 30, "bike": 10, "bus": 50}
        v = input("Vehicle (car/bike/bus): ").lower()
        if v not in rate:
            print("Invalid vehicle")
        else:
            fee = min(500, int(hours + 0.99) * rate[v])
            print("Parking fee: ₹", fee)
except ValueError:
    print("Invalid time format")