#🧩 Challenge 3: Loop Counter with Stop

#Start a number at 1, keep adding 1, and print the number — but stop at 10 without printing number 7.

number = 0

while number < 10:
  
  number += 1
  if number == 7:
    continue
  print(number)