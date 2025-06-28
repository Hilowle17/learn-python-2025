#🔹 PART 5: Return True or False (Boolean Functions)
#Theory:
#Functions can return yes/no answers.

def is_even(n):
    return n % 2 == 0
even_or_not = is_even(6)
print("Result:", even_or_not)
#This gives True for even, False for odd
    
#Used in filtering, logic checks, permissions

#✅ You don’t need if/else — just return the comparison.

#💬 Real-world use:
is_even(13)
def is_valid_password(password):
    return len(password) >= 8
