grade1 = 78
grade2 = 85
grade3 = 92
grade4 = 67
grade5 = 88
full_percantage = 100
total_subject = 5
total_score = grade1 + grade2 + grade3 + grade4 + grade5

percantage1 = (grade1/total_score)*full_percantage
percantage2 = (grade2/total_score)*full_percantage
percantage3 = (grade3/total_score)*full_percantage
percantage4 = (grade4/total_score)*full_percantage
percantage5 = (grade5/total_score)*full_percantage

average_score = (total_score/total_subject)

print(f"GRADE 1 = {grade1}")
print(f"GRADE 2 = {grade2}")
print(f"GRADE 3 = {grade3}")
print(f"GRADE 4 = {grade4}")
print(f"GRADE 5 = {grade5}")
print(f"")
print(f"Percantage grade1 = {percantage1}")
print(f"Percantage grade2 = {percantage2}")
print(f"Percantage grade3 = {percantage3}")
print(f"Percantage grade4 = {percantage4}")
print(f"Percantage grade5 = {percantage5}")
print(f"")
print(f"Average Score = {average_score}")
print(f"Total Score = {total_score}")

