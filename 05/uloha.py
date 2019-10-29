zvierata = ["had", "andulka", "jelen", "opica"]

zvierata2 = []

for zviera in zvierata:
    zvierata2.append((zviera[1:], zviera))

print(zvierata2)

zvierata2.sort()
print(zvierata2)

zvierata.clear()

for zviera_dvojice in zvierata2:
    zvierata.append(zviera_dvojice[1])

print(zvierata)
