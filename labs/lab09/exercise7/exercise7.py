student_gpa = float(input())
total_score = int(input())
number_extracurricular = int(input())  
completed_interview = input().strip()  

# TODO: Your code here
requirements_met = 0

if student_gpa >= 3.0:
    requirements_met += 1
if total_score >= 1200:
    requirements_met += 1
if number_extracurricular >= 1:
    requirements_met += 1
if completed_interview == "Yes": 
    requirements_met += 1


if requirements_met == 4:
    admission_status = "Accepted"
elif requirements_met == 3:
    admission_status = "Waitlisted"
else:
    admission_status = "Rejected"

print(admission_status)
