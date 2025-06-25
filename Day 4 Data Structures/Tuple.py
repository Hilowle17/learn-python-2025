#🔷 PART 2: tuple — Ordered and Unchangeable

#🧠 Explanation:

  #A tuple is like a list, but you can’t change it.

  #It’s useful when the data should never be modified.

#In real life:

  #Months of the year → ("Jan", "Feb", "Mar", ...)

  #Gender options → ("Male", "Female", "Other")

#You use a tuple when:

  #You want to protect the data.

  #You want to write faster code with less memory.

#💻 Code:

# Creating a tuple
months = ("January", "February", "March")

# Accessing values
print(months[1])  # February

# You can't do this:
# months[1] = "April"  ❌ Error



# A tuple of months
months = ("Jan", "Feb", "Mar", "Feb")

# Count how many times 'Feb' appears
print("Feb appears:", months.count("Feb"))

# Find the index of 'Mar'
print("Index of Mar:", months.index("Mar"))

# Note: You can't add, remove, or change items in a tuple!
