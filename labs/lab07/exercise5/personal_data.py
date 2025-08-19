# personal_data.py

import random
import math

# Personal information variables
full_name = "Christian Geronimo"
age = 18
height_cm = 175
weight_kg = 50
phone_number = "0123456789"
email_address = "chris@example.com"
address = "Lorong 5 Kota Samarahan"
city = "Kuching"
postcode = "93000"

# String operations
name_upper = full_name.upper()
name_lower = full_name.lower()
name_length = len(full_name)

city_upper = city.upper()

# Full address: combine street + city + postcode
full_address = f"{address}, {city}, {postcode}"
full_address_length = len(full_address)
