n = int(input("Enter number of products: "))

for i in range(n):
    name = input("Product name: ")
    opening = int(input("Opening stock: "))
    incoming = int(input("Incoming stock: "))
    dispatched = int(input("Dispatched stock: "))
    closing = int(input("Actual closing stock: "))

    expected = opening + incoming - dispatched
    print("Product:", name)
    print("Expected stock:", expected)

    if closing == expected:
        print("Stock matches")
    else:
        print("Discrepancy:", closing - expected)

    reorder = max(0, 50 - closing)
    print("Replenishment required:", reorder)