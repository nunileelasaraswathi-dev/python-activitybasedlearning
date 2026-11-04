balance = float(input("Enter initial balance: "))
limit = 5000
transactions = []

n = int(input("Enter number of transactions: "))

for i in range(n):
    typ = input("Enter deposit/withdraw: ").lower()
    amt = float(input("Enter amount: "))

    if amt <= 0:
        print("Invalid amount")
    elif typ == "deposit":
        balance += amt
        transactions.append("Deposit: " + str(amt))
    elif typ == "withdraw":
        if amt <= balance and amt <= limit:
            balance -= amt
            transactions.append("Withdraw: " + str(amt))
        else:
            print("Withdrawal rejected")
    else:
        print("Invalid transaction")

print("\nTransactions:", transactions)
print("Final balance:", balance)