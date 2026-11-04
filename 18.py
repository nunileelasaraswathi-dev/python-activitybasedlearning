n = int(input("Number of vehicles: "))
distance = float(input("Journey distance (km): "))
price = float(input("Fuel price per litre: "))
reserve = float(input("Reserve fuel (litres): "))

best = None

for i in range(n):
    name = input("Vehicle name: ")
    mileage = float(input("Mileage (km/l): "))
    fuel = distance / mileage + reserve
    cost = fuel * price
    print(name, "Fuel:", round(fuel, 2), "Cost:", round(cost, 2))

    if best is None or cost < best[1]:
        best = (name, cost)

print("Lowest-cost option:", best[0], "Cost:", round(best[1], 2))