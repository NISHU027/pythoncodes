import re

# Open file
file = open("data.txt", "r")
data = file.read()

# Regex patterns
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', data)
phones = re.findall(r'[6-9]\d{9}', data)
dates = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', data)

# Display results
print("Emails found:")
for e in emails:
    print(e)

print("\nPhone numbers found:")
for p in phones:
    print(p)

print("\nDates found:")
for d in dates:
    print(d)

file.close()