#Requirements:
#In a file called grocery.py, implement a program that prompts the user for items, one per line,
# until the user inputs control-d (which is a common way of ending one’s input to a program).
# Then output the user’s grocery list in all uppercase, sorted alphabetically by item,
# prefixing each line with the number of times the user inputted that item.
# No need to pluralize the items. Treat the user’s input case-insensitively.

#Count item frequencies
from collections import Counter

#dict-like mapping with default 0
item_frequency = Counter()

while True:
    try:
        item = input().strip() #Read a line and strip surrounding whitespace
    except EOFError: #Ctrl+D scenario; need to break
        break
    if not item: #Skip empty/whitespace-only lines
        continue
    item_frequency[item.lower()] += 1 #Normalize key to lowercase and increment its count.

for item in sorted(item_frequency): #Iterate over keys sorted alphabetically
    print(item_frequency[item], item.upper()) #Print count and item name in uppercase

