# menu_data.py

import random

# Restaurant details
Restaurant_name = "Tropical Bites"
restaurant_location = "Kuching"

# Menu items (names only)
menu_item1 = "Nasi Lemak"
menu_item2 = "Laksa Sarawak"
menu_item3 = "Roti Canai"

# String operations
name_upper = Restaurant_name.upper()
name_lower = Restaurant_name.lower()
location_length = len(restaurant_location)

# Random numbers
daily_special = random.randint(1, 3)  # special item: 1, 2, or 3
customer_number = random.randint(100, 999)  # customer number: 100-999
