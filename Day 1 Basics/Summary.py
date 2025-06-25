# Welcome message
print("Welcome to Day 1, Mr. Execution 💻")

# Ask user info
name = input("What is your name? ")
age = int(input("How old are you? "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"
Student_age = int(input("How old are you: ")) >= 18

# Show the data
print("Name:", name)
print("Age:", age)
print("Student:", is_student)
print("Student ID:", Student_age)

# Show types
print(type(name))         # <class 'str'>
print(type(age))          # <class 'int'>
print(type(is_student))   # <class 'bool'>
print(type(Student_age))   # <class 'bool'>
