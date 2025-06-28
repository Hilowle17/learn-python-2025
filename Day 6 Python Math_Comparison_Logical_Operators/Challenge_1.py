#🔹 Challenge 1: Age Checker
#Ask the user for age. If the user is 18 or older, say "Adult". Else, say "Minor".

age = int(input("How old are You? : "))
if age >= 18:
  print("adult")
elif age < 18:
  print("Minor")
  