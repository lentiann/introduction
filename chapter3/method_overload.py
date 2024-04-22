class Calculator:
    def add(self, a=0, b=0):
        return a + b

    def add(self, a=0, b=0, c=0):
        return a + b + c
    
calculator = Calculator()
print(calculator.add(1, 2))
print(calculator.add(1, 2, 3))