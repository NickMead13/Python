import re

count = int(input("input data:"))

results = ''
for i in range(count):
    val = input()
    # Use regular expression to remove all non-alphanumerical characters
    val = re.sub('[^A-Za-z0-9]', '', val)
    # Replace all letters with lowercase to avoid case sensitive
    val = val.lower()
    if (val == val[::-1]):
        results = results + "Y "
    else:
        results = results + "N "

print(results)
