#🔹 PART 4: Default Parameters
#Theory:

#Sometimes you want to make inputs optional.

#You give a default value in case nothing is passed.

def greet(name="Guest"):
    print("Welcome,", name)

greet()             # uses default
greet("Mohamed")    # uses actual name
#💬 Real-world use:

def send_email(to, subject="No Subject"):
    print("Sending to:", to, "with subject:", subject)
