#🔁 1. for Loop

#✅ What it does:
#Repeats a block of code a specific number of times (when you know how many times).

#✅ Syntax:

#for variable in iterable:
    # code block

#✅ Common Use:

for i in range(5):
    print("Hello", i)

for tiro in range(20):
    print(tiro)
for name in ["Ali", "Ayan", "Ahmed"]:
    print(name)

#❓ Questions:


#What does range(5) do?	Creates numbers 0 to 4 (5 is not included)
#What is the output of for i in range(3): print(i)?	0\n1\n2
#Can you use for with a list?	Yes: for name in ["Ali", "Ayan"]: print(name)
#What is an iterable?	Something you can loop over (list, range, string)


#🔄 2. while Loop
#✅ What it does:
#Repeats as long as a condition is True.

#✅ Syntax:

#while condition:
    # code block
#✅ Example:

x = 2
while x <= 100:
    print(x)
    x += 2

#❓ Questions:

#When do you use while instead of for?	When you don’t know how many times to repeat
#What happens if the condition never becomes False?	Infinite loop
#How to stop an infinite loop manually?	Press Ctrl + C in the terminal


#🛑 3. break Statement

#✅ What it does:
#Exits the loop immediately, even if the condition is still True.

#✅ Example:

for i in range(10):
    if i == 5:
        break
    print(i)

#❓ Questions:

#What does break do?	Stops the loop early
#What is the output of above code?	0\n1\n2\n3\n4


#➿ 4. continue Statement

#✅ What it does:
#Skips the current iteration and moves to the next one.

#✅ Example:

for i in range(5):
    if i == 2:
        continue
    print(i)
#❓ Questions:

#What does continue do?	Skips the current step and continues
#What is the output of above code?	0\n1\n3\n4 (2 is skipped)

#🔁 5. Looping Through Different Types

#✅ Looping through a string:

for char in "Python":
    print(char)

#✅ Looping through a list:

names = ["Ali", "Amina", "Ahmed"]
for name in names:
    print("Hello", name)

#❓ Questions:

#Can we loop through a string?	Yes, it is iterable
#How to loop through list values?	for item in list:


#🧨 6. else with Loops (Advanced)

#Yes — Python allows an else block with loops!

#✅ Example:

for i in range(3):
    
    print(i)
else:
    print("Loop completed!")
#❓ Questions:

#When does the else block run?	When the loop finishes normally (not with break)
#What happens if the loop breaks?	else block is skipped

#🚫 pass Statement
#It means “do nothing” — used when Python needs a line but you don’t want to do anything yet.

#Example:

for i in range(3):
    pass