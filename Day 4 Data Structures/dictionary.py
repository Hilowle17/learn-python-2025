#🟨 PART 4: dict — Key → Value Mapping

#🧠 Explanation:

  #A dictionary (or dict) is the most powerful structure.
  #It stores data as pairs:

    #A key (like a label)

    #A value (the data)

#Example:

{
  "name": "Mohamed",
  "age": 24,
  "is_student": True
}
#You use dict when you want to store info about something — like:

#A person

#A book

#A product

#A course

#Keys must be unique, and you use the key to get the value.

#💻 Code:

# Creating a dictionary
student = {
  "name": "Mohamed",
  "age": 24,
  "is_student": True
  
}

# Accessing values
print(student["name"])

# Changing values
student["age"] = 25

# Adding a new key
student["city"] = "Mogadishu"

# Printing whole dictionary
print(student)



# Student dictionary
student = {
    "name": "Mohamed",
    "age": 23,
    "course": "Python"
}
print("Original:", student)

# Update the course
student["course"] = "JavaScript"
print("After course update:", student)

# Add a new key-value
student["city"] = "Mogadishu"
print("After adding city:", student)

# Get value safely
print("Course (via get):", student.get("course"))

# Get all keys
print("Keys:", student.keys())

# Get all values
print("Values:", student.values())

# Get all items
print("Items:", student.items())

# Remove age
student.pop("age")
print("After pop age:", student)
