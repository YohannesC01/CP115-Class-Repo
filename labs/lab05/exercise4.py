print("Welcome to the Shopping cost calculator!")
print("This program will calculate the shopping cost.")

Item_name1 = input("Enter Item name: ")
Price1 = float(input("Enter the Price: "))
Quantity1 = float(input("Enter Quantity of item: "))

Item_name2 = input("Enter Item name: ")
Price2 = float(input("Enter the Price: "))
Quantity2 = float(input("Enter Quantity of item: "))

Item_name3 = input("Enter Item name: ")
Price3 = float(input("Enter the Price: "))
Quantity3 = float(input("Enter Quantity of item: "))

Tax_rate = float(input("Enter tax rate: "))

Total = float(Price1 * Quantity1 + Price2 * Quantity2 + Price3 * Quantity3)
Tax = float(Total * Tax_rate)
Total_Cost = Total + Tax

print()
print("Price item 1: " + str(Price1))
print("Price item 2: " + str(Price2))
print("Price item 3: " + str(Price3))
print("Total: " + str(Total))
print("Tax: " + str(Tax))
print("Total Cost: " + str(Total_Cost))
