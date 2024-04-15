#Strukturat e te dhenave ne Python jane # list, tuples, sets dhe dictionaries.

# Lista jane mutable (Te ndryshushme) edhe mund te ndryshoj me vone, dhe lejon elemente te njejta(Duplicates).
# Tuples jane immutable (Te pandryshushme) dhe nuk lejon elemente te njejta.
# Sets jane mutable (Te ndryshushme) dhe nuk lejon elemente te njejta.
# Dictionaries jane mutable (Te ndryshushme) dhe lejon elemente te njejta.

names = ["alentian", "blentian", "alentiana"]

print("----")
print(names)

names.append("lentian1")

print("----")
print(names)

names.remove("lentian")

print("----")
print(names)

names.insert(0, "lentian2")

print("----")
print(names)

names.sort() # A-Z
names.sort(reverse=True) # Z-A

names.reverse()

print("----")
print(names)

name = names.pop()

print("----")
print(names)
print("-------------------------")
print(name)