import re
d = []
f1 = open("cat.txt","r").read()
f1 = re.sub(r'(?mis)\s','',f1)
print f1

