import re

match = re.search(r"\d", "a fost o zi de pomina")
print(match)
#print(match.span()) #Starting and endig index of the object we searched for
print(match.string) #Stringul in care am cautat
print(match.group()) #Sub-Stringul care fittuie cel mai bine in stringul in care suntem
print(match.groups())
print(match.string[0])

# print("1\n2")
# print("1\\n2")
# print(r"1\n2")

# ---------------------------------------------------
# match = re.findall(r"zi", "a fost o zi de pomina")
# print(match)

# ----------------------------------------------------

# #match = re.split(r"zi", "a fost o zi de pomina")
# match = re.split(r"zi", "prefiXziSufix")
# print(match)


# ----------------------------------------------------

# match = re.sub(r"zi", "parasinus", "a gost o zi de pomina")
# print(match)