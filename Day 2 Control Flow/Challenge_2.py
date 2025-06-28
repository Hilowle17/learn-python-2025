#🎯 Challenge 2: Smart Login System

#Create a smart login system that behaves differently based on the user’s role, age, and student status.

#👨‍💻 What Your Program Should Do:
#Ask the user for:

#Full name (str)

#Age (int)

#Are they a student? (yes/no) → convert to Boolean

#User role → input can be: admin, moderator, or user

#Based on the inputs, make decisions:

#If age is under 13 → print "Access denied: Too young."

#If role is admin and age >= 18 → print "Welcome Admin! You have full access."

#If role is moderator and age >= 16 → print "Moderator access granted."

#If user is a student and age >= 18 → print "Student user: limited access."

#Otherwise → print "Access granted: General user."

full_name = input("Enter Your Full Name: ")
age = int(input("How old are You?" ))
is_student = input("are You a Student? (Yes/No) ").lower == "yes"
role = input("Enter your role (admin/moderator/user): ").lower()

while role not in ["admin", "moderator", "user"]:
    print("Invalid role! Please enter admin, moderator, or user.")
    role = input("Enter your role (admin/moderator/user): ").lower()


if age < 13:
    print("Access denied: Too young.")
elif role == "admin" and age >= 18:
    print("Welcome Admin! You have full access.")
elif role == "moderator" and age >= 16:
    print("Moderator access granted.")
elif role == "user" and age >= 18:
    print("Student user: limited access.")

else:
    print("Access granted: General user.")
