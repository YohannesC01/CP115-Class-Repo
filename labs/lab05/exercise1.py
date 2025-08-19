print("Welcome to the Student information system!")
print("This program will show your Information.")

# Getting user input (always returns a string)
student_name = input("Enter your name: ")
Student_age = input("Enter your age: ")
course_code = input("Enter your course code: ")

# Formatted output using string concatenation
print()
print("Student: " + student_name)
print("Age: " + Student_age)
print("Course Code: " + str(course_code))

print(type(student_name))
print(type(Student_age))
print(type(course_code))