monthly_income = int(input())
employment_status = input().strip().lower()
credit_rating = input().strip().lower()
employment_years = int(input())

# TODO: Your code here
criteria_met = 0

if monthly_income >= 3000:
    criteria_met += 1
if employment_status in ["permanent", "contract"]:
    criteria_met += 1
if credit_rating in ["good", "excellent"]:
    criteria_met += 1
if employment_years >= 2:
    criteria_met += 1

if criteria_met == 4:
    approval_status = "Approved"
elif criteria_met == 3:
    approval_status = "Conditionally Approved"
else:
    approval_status = "Rejected"

print(approval_status)
