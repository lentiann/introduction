names = ["lentian", "lentian1", "lentian2", "lentian3"]

print(f"Personi 1: {names[0]} ")
print(f"Personi 2: {names[1]} ")
print(f"Personi 3: {names[2]} ")
print(f"Personi 4: {names[3]} ")

print("-------------------------------------------------")
for name in names:
    print(f"Personi 1: {name}")

print("-------------------------------------------------")
for index in range(0, len(names)):
    print(f"Personi {index + 1}: {names[index]}")
    
print("-------------------------------------------------")
for index, name in enumerate(names):
    print(f"Personi {index + 1}: {name}")

is_found = False
for name in names:
    if name == "lentian2":
        is_found = True
        break
    
if is_found:
    print("Personi u gjet")
else:
    print("Personi nuk u gjet")

for name in names:
    if name == "lentian2":
        continue
    print(name)