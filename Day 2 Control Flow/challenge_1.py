# Challenge 1: Who Are You?

#Ask the user:

#Name
#Age
#Are you a student?

#Then decide:

#If under 18 → say "Minor"

#If student and over 18 → "Adult Student"

#If not a student and over 18 → "Adult, not a student"

name = input("Enter Your Name: ")
age = int(input("How old are You? "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

if age < 18:
  print("You are Minor")
elif is_student and age >= 18:
    print("Adult Student")
else:
  print("Adult, not a student")