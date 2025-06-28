#🔹 Challenge 2: Student Discount
#Ask:

#Age

#Is student? (yes/no)

#If student and age < 25 ➝ "Discount Applied"

#Else ➝ "No discount"

age = int(input("How old are you? : "))
is_student = input("Are you a student?(yes/no) : ").lower() == "yes"
if age < 25 and is_student:
  print("Discount applied")
else:
  print("No Discount")