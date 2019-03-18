import re

regex = input("Enter Pattern :")
pattern = re.compile(regex)

while True:
    data = input("Enter String:")
    m = pattern.search(data) # searches entire string for the pattern
    if m:
        print("match found")
        print(" ",m.span(),m.group())
    else:
        print("match not found")