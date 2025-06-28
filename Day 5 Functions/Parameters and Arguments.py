#🔹 PART 2: Parameters & Arguments

#Theory:

#A parameter is like asking for input when defining the function.

#An argument is what you actually send when using it.

def greet(name):     # "name" is a parameter
    print("Hello", name)

greet("Ayaan")       # "Ayaan" is an argument
#✅ You can use any name like username, guest, student_name, etc.

#💬 Real-world use:

def calculate_price(price, tax):
    return price + (price * tax)

#Here price and tax are parameters → you’ll pass different prices/values later.

