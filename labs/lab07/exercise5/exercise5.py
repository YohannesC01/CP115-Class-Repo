# exercise5.py

import personal_data

print("=== Personal Profile ===")
print(f"Full Name: {personal_data.full_name}")
print(f"Age: {personal_data.age} years")
print(f"Height: {personal_data.height_cm} cm")
print(f"Weight: {personal_data.weight_kg} kg")
print(f"Phone: {personal_data.phone_number}")
print(f"Email: {personal_data.email_address}")
print(f"Adress: {personal_data.address}")
print()


print(f"Name in UPPERCASE: {personal_data.name_upper}")
print(f"Name in lowercase: {personal_data.name_lower}")
print(f"Length of Name: {personal_data.name_length} characters")
print(f"City in UPPERCASE: {personal_data.city_upper}")
print()


print(f"Full Address: {personal_data.full_address}")
print(f"Length of Address: {personal_data.full_address_length} characters")
