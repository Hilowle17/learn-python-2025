#✅ 1. if Statement (The Brain Trigger)

#🔹 Syntax:

#if condition:
    # do something

#🔸 Example:

age = 20
if age > 18:
    print("You're an adult.")

#🤔 Questions:
#Q: What does if do?
#A: It checks if a condition is True, then runs the code inside.

#Q: What if the condition is False?
#A: It skips that block.


#✅ 2. else (Backup Plan)

#🔹 Syntax:

#if condition:
    # do this
#else:
    # do this instead

#🔸 Example:

is_student = True
if is_student:
    print("Welcome student!")
else:
    print("Welcome guest!")

#🤔 Questions:

#Q: Is else required?
#A: No, it’s optional. Use it when you want a fallback.


#✅ 3. elif (Check More Than One)

#🔹 Syntax:

#if condition1:
    # do this
#elif condition2:
    # do this
#else:
    # fallback

#🔸 Example:

age = 17
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")

#🤔 Questions:
#Q: Can I use many elif?
#A: Yes, as many as you need.

#Q: What if multiple elif are True?
#A: Python runs the first one only and skips the rest.