#🧩 Challenge 2: Password Attempt

#Ask user for password until they enter "123". When correct, say: "Access Granted".

password = "123"

while True:
 check = input("Enter Your Password: ")
 if check == password:
  print("Access Granted")
  break
 else:
  print("Wrong password")
  continue