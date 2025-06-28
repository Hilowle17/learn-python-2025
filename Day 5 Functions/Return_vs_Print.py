#🔹 PART 3: Return vs Print
#Theory:

#print()	                    return
#Shows result to user	        Gives result back to the code
#One-time output	            Can be saved and reused
#Used in UI	                  Used in calculations, logic

def add(a, b):
    return a + b

total = add(3, 5)
print("Result:", total)
#✅ Always use return if you want to use the result later.

#💬 Real-world use:
#In a banking app:

def check_balance(account):
    return 5000
#You don't print balance inside the function. You return it → then display or store it.

