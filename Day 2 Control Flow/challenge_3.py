#🎯 Challenge 3: The Smart Profile Evaluator

#🎯 Goal:
#Create a program that collects user profile information and gives a custom personality report based on logic and answers.

#🧠 What to Ask the User:
#Full Name

#Age (convert to int)

#Are you a student? (yes/no → convert to bool)

#Your favorite color (red, blue, or green) → validate input (with loop)

#Do you like programming? (yes/no → convert to bool)

#🧾 Rules / Logic for Response:

#🔸 Part 1 – Age Group
#If age < 13 → "You are a creative child 👶"

#If age between 13–19 → "Teen thinker 🧠"

#If age >= 20 → "Adult learner 👨‍💻"

#🔸 Part 2 – Color Personality

#If color is "red" → "You are energetic 🔴"

#If color is "blue" → "You are calm 🔵"

#If color is "green" → "You are balanced 🟢"

#🔸 Part 3 – Programming Affinity

#If likes programming and is student → "You're on the path to greatness 🚀"

#If not student and likes programming → "Lifelong learner mode 🔥"

#If doesn't like programming → "No worries, tech still loves you ❤️"




full_name = input("What is your Full Name: ")
age = int(input("How old are you? "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"
color = input("Enter your color (red/blue/green): ").lower()
while color not in ["red", "blue", "green"]:
    color = input("Enter your color (red/blue/green): ").lower()
like_programming = input("Do you like Programming? ").lower() == "yes"

print("Hello, "+ full_name)

if age < 13:
    print("👤 Age Group: You are a creative child 👶")
elif age > 13 and age < 19:
    print("👤 Age Group: Teen Thinker 🧠")
elif age >= 20:
    print("👤 Age Group: Adult learner 👨‍💻")

if color == "red":
    print("🎨 Personality Color: You are energetic 🔴")
elif color == "blue":
    print("🎨 Personality Color: You are calm 🔵")
elif color == "green":
    print("🎨 Personality Color: You are balanced 🟢")

if like_programming and is_student:
    print("💻 Programming Spirit: You're on the path to greatness 🚀")
elif like_programming:
    print("💻 Programming Spirit: Lifelong learner mode 🔥")
else:
    print("💻 Programming Spirit: No worries, tech still loves you ❤️")
