budget = float(input("Enter budget: "))
n = int(input("Number of products: "))
total = 0

for i in range(n):
    name = input("Product name: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    cost = price * qty

    if qty > 0 and price >= 0 and cost > 500:
        cost *= 0.90

    total += cost
    print(name, "Cost:", round(cost, 2))

print("Total:", round(total, 2))
if total > budget:
    print("Reduce purchases by:", round(total - budget, 2))
else:
    print("Within budget")