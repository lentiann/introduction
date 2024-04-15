
fruits = ("banana", "apple", "cherry")
random_tuple = ("apple", 1, 2, 3, True, False)
integer_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

fruits_random_tuple = random_tuple + fruits

print(f"Random Tuple: {random_tuple}")
print(f"Combined Tuple: {fruits_random_tuple}")

if "apple" in fruits:
    print("Yes, 'apple' is in the fruits tuple")
else:
    print("No, 'apple' is not in the fruits tuple")
    
sub_fruits = fruits[0:2]
complete_fruits = fruits[0:]
skip_first_fruits = fruits[1:]
last_fruits = fruits[-1::-1]


print(f"Sub Fruits: {sub_fruits}")
print(f"Complete Fruits: {complete_fruits}")
print(f"Skip Fruits: {skip_first_fruits}")
print(f"Last Fruits: {last_fruits}")

print("Max ne tuple integer: ", max(integer_tuple))
print("Min ne tuple integer: ", min(integer_tuple))
print("Gjatesia ne tuple integer: ", len(integer_tuple))