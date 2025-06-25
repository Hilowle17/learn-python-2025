#✅ 6. Nested Conditions (if inside if)

#🔹 Example:

age = 17
is_student = True

if age > 18:
    if is_student:
        print("Adult student")
    if age < 18:
        print("You are Not Adult student") 
    else:
        print("Adult non-student")

#🤔 Questions:

#Q: When should I nest if?
#A: When one condition depends on another.