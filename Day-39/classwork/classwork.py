Price = int(input("How much does the item cost: "))
Discount = int(input("Whats the discount: "))

discount = int(Price * Discount / 100)
New_price = Price - discount
print("New price is", New_price)
