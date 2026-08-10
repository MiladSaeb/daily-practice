delare = ("==============================================================================================================")
with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()
ord = text.split()
print(ord)

print(delare)

antal = {}

for o in ord:
    if o in antal:
        antal[o] = antal[o] + 1
    else:
        antal[o] = 1

print(antal)
print(delare)

sorterat = sorted(antal.items(), key=lambda x: x[1], reverse=True)
print(sorterat[:3])