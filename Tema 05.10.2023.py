# Input string
input_phrase = "I am writing something that I will probably use later on"

# Split the string into words
words = input_phrase.split()

# Remove the second and third words (index 1 and 2)
del words[1:3]

# Join the remaining words back into a string
result = ' '.join(words)

# Print the result
print(result)