#Klasa eshte blueprint i nje objekti. Klasa mund te permbaje metoda dhe atribute.
#Klasa mund te krijoje objekte te reja duke perdorur konstruktorin e klases.
#Nje objekt eshte nje instance e klases.
#Nje instance eshte nje objekt i krijuar nga nje klase.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def eat(self):
        return "Yum yum yum"
    
    def walk(self):
        return "I am walking"
    
    def talk(self):
        return "I am talking"


person = Person("Alice", 25)
print(person)
print(person.get_age())
print(person.get_name())
print(person.eat())