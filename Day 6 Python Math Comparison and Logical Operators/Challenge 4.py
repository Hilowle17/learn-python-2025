#🔹 Challenge 4: Word Counter
#Ask user to enter a sentence.

#Count how many times the word “python” appears.


sentence = input("Enter a sentence: ").lower()

count = sentence.count("python")

print(f"The word 'python' appeared {count} times.")
