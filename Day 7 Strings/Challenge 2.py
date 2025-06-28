#🔹 Challenge 2: Password Cleaner
#Ask the user to enter a password.

#Remove leading/trailing spaces.

#If password is "python123" after cleaning, say "✅ Access".

#Else say "❌ Wrong Password".

password = input("Enter your password: ").strip()

if password == "python123":
    print("✅ Access")
else:
    print("❌ Wrong Password")