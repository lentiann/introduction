# please make examples for teaching python basic and oop on livestream twitch i already convered:

# variables, operators(logical,bitwise) etc.


# Example 1: Hello World
print("Hello, World!")

# Example 2: User Input
name = input("Enter your name: ")
print("Hello,", name)

# Example 3: Conditional Statements
x = 10
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

# Example 4: Loops
for i in range(5):
    print(i)


# Example 5: Functions
def add_numbers(a, b):
    return a + b


result = add_numbers(3, 5)
# Example 6: Printing a Result
print("The result is:", result)

# Example 7: Working with Lists
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print("Number:", number)

# Example 8: Working with Dictionaries
person = {"name": "John", "age": 25, "city": "New York"}
print("Person:", person)


# Example 9: Creating a Class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hello, my name is", self.name)

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age})"


# Example 10: Creating an Object
student = Student("Alice", 20)
student.introduce()
