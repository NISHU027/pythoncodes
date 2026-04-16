# Open file in read mode
file = open("sample.txt", "r")

# Read file content
data = file.read()

# Split into words
words = data.split()

# Take length input from user
length = int(input("Enter word length: "))

print("Words with length", length, ":")

# Check each word
for word in words:
    if len(word) == length:
        print(word)

# Close file
file.close()