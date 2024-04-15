fruits = {"banana", "apple", "cherry"}
passion_fruits = {"coconut", "mango", "ananas"}

print(fruits)

if "apple" in fruits:
    print("Yes, 'apple' is in the fruits set")
else:
    print("No, 'apple' is not in the fruits set")

# fruits.add("orange")
# print(fruits)

fruits.update(passion_fruits)
print(fruits)

combined_fruits = fruits | passion_fruits

union_fruits = fruits.union(passion_fruits)

print(combined_fruits)
print("------------------------------")
print(union_fruits)

# fruits.discard("x")
# print(fruits)

# fruits.clear()

# print(fruits)

# intersection_fruits = fruits.intersection(passion_fruits)
# print(intersection_fruits)