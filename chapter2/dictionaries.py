fruits_dict = {"banana": 1, "apple": 2, "cherry": 3}

print(fruits_dict)
# print(fruits_dict["banana1"])

if fruits_dict.get("banana"):
    print("Yes, 'banana' is in the fruits dictionary")
    print(f"Value of Banana: {fruits_dict['banana']}")
else:
    print("No, 'banana' is not in the fruits dictionary")
    
fruits_dict["orange"] = 4
print(fruits_dict)

for key, value in fruits_dict.items():
    print(f"Key: {key}, Value: {value}")

print("-------------------------")

for key in fruits_dict.keys():
    print(f"Key: {key}")

print("-------------------------")
for item in fruits_dict.values():
    print(f"Value: {item}")