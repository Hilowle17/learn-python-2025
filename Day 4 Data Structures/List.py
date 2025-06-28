#🔶 PART 1: list — Ordered and Changeable

#🧠 Explanation:

#A list is a collection — like a box — where you can store multiple values.

#These values are kept in order (1st, 2nd, 3rd...) and you can change them any time:

#You can add new values.

#You can remove values.

#You can update values.

#You can even loop through all values to do something with each.

#In real life:

#A shopping list: ["bread", "milk", "eggs"]

#List of users: ["Ali", "Mohamed", "Fatima"]

#List of scores: [88, 76, 90]

#Each item has a position, starting from 0. That’s called the index.

#💻 Code:

# Creating a list
foods = ["Rice", "Meat", "Banana", "Rice"]

# Accessing items
print(foods[0])  # Rice

# Adding items
foods.append("Fish")

# Removing items
foods.remove("Meat")

# Changing a value
foods[1] = "Apple"

# Printing everything
print(foods)
foods.reverse()
foods.count("Rice")
print(foods)


# Start with a list of foods
foods = ["Rice", "Meat", "Milk"]
print("Original:", foods)

# Add new food
foods.append("Banana")
print("After append:", foods)

# Insert a new food at position 1
foods.insert(1, "Fish")
print("After insert:", foods)

# Remove a food
foods.remove("Milk")
print("After remove:", foods)

# Reverse the list
foods.reverse()
print("After reverse:", foods)

# Count how many times 'Rice' appears
print("Count of Rice:", foods.count("Rice"))

# Index of 'Fish'
print("Index of Fish:", foods.index("Fish"))
