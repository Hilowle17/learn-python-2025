#🟩 PART 3: set — Unordered and Unique

#🧠 Explanation:

  #A set is a collection that:

    #Doesn’t allow duplicates

    #Doesn’t keep order

#In real life:

  #Unique phone numbers

  #Unique colors

  #Unique user IDs

#If you try to add the same item twice, it will automatically remove duplicates.

#Useful when:

  #You only care what is in the data, not the order.

  #You don’t want repeated values.

#💻 Code:

# Creating a set
colors = {"red", "green", "blue", "red"}

# Output will be only unique values
print(colors)  # {'red', 'green', 'blue'}

# Add new color
colors.add("yellow")

# Remove color
colors.remove("green")

print(colors)



# Set of colors
colors = {"red", "blue", "blue"}
print("Original:", colors)  # Duplicates removed

# Add a color
colors.add("green")
print("After add:", colors)

# Remove a color
colors.remove("red")
print("After remove:", colors)

# Discard a color (safe even if not found)
colors.discard("blue")  # No error
print("After discard:", colors)

# Clear all colors
colors.clear()
print("After clear:", colors)
