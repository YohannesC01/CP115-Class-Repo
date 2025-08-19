# exercise4.py

import menu_data

print(f"=== Welcome to {menu_data.Restaurant_name}! ===")
print(f"Hello Customer #{menu_data.customer_number}")
print()

print("Our Menu Today:")
print(f"1. {menu_data.menu_item1}")
print(f"2. {menu_data.menu_item2}")
print(f"3. {menu_data.menu_item3}")
print()

# Pick today's special using daily_special number
if menu_data.daily_special == 1:
    special = menu_data.menu_item1
elif menu_data.daily_special == 2:
    special = menu_data.menu_item2
else:
    special = menu_data.menu_item3

print(f"Today's Special: {special}")
