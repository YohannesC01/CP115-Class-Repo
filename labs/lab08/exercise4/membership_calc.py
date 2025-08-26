monthly_membership_cost = 120
personal_training_cost = 80
personal_training_session = 6
locker_rental = 25
towel_service = 15
onetime_membership_cost = 50
annual_month = 12

first_month = onetime_membership_cost + monthly_membership_cost + (personal_training_cost*6) + locker_rental + towel_service
after_first_month = monthly_membership_cost + (personal_training_cost*6) + locker_rental + towel_service
annual_cost = (monthly_membership_cost + (personal_training_cost*6) + locker_rental + towel_service)*annual_month

print(f"{first_month}")
print(f"{after_first_month}")
print(f"{annual_cost}")