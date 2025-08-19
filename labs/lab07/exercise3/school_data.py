# school_data.py

import random
import math

# Student information
student_name = "Christian"
student_id = "S12345"
age = 20

# Course information
course_code = "CS101"
course_name = "Jurusan Sains Komputer"

# Generate random scores
score1 = random.randint(70, 95)
score2 = random.randint(75, 100)

# Calculate total score
total_score = score1 + score2

# String operations on student name
name_upper = student_name.upper()
name_lower = student_name.lower()
name_length = len(student_name)

# Calculate square root of total score
sqrt_total_score = math.sqrt(total_score)
