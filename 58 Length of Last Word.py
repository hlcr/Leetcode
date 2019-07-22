import re
line =  "Cats are smarter than do-gs"
pattern = re.compile("[a-zA-Z\-]+")
r = pattern.findall(line)
print(r)