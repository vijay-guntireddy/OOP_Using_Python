import re
regex = r"""




"""

pattern = re.compile(regex,re.VERBOSE|re.DOTALL|re.MULTILINE)
while True:
    content = input("enter time")
    print(content)
    pattern.search(content)



