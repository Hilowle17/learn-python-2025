print("Welcome to Python Day 1, Mr. Execution 🧠")
FullName = (input("Enter your full name: "))
age = int(input("Enter your age:"))


is_student = input("Are you a student? (yes/no): ").lower() == "yes"

print("👤 Name: ",FullName)
print("🎂 Age: ",age)
print("🎓 Student: ", is_student)

if age >= 18:
  
  print("You are an adult.")
else:
  print("You are a minor.")

print(type(FullName))
print(type(age))
print(type(is_student))
print(type(age))
