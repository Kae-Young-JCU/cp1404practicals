itemQuantity = int(input("Number of items: "))
while itemQuantity < 0:
    print("Invalid entry. Number of items must be 0 or greater.")
    itemQuantity = int(input("Number of items: "))
totalCost = 0
for i in range(0, itemQuantity, 1):
    itemPrice = float(input("Price of item: "))
    totalCost += itemPrice
if totalCost > 100:
    totalCost = 0.9*totalCost
totalCostFormatted = "{:.2f}".format(totalCost)
# print("Total price for " + itemQuantity + " items is $" + totalCost) <-- I miss c# :(
print(f'{"Total price for "}{itemQuantity}{" items is $"}{totalCostFormatted}')
