# We want to calculate the salary of employees in a company, where we have different types of employees:
# - Salaried employees: they have a fixed salary
# - Hourly employees: they have an hourly rate and the number of hours worked
# - Contractor emplyoees: Houraly rate and number of hours worked, but they have a fixed bonus

from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def calculate_bonus(self):
        pass

    def calculate_total_salary(self):
        return self.calculate_salary() + self.calculate_bonus()


class FullTimeEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def calculate_salary(self):
        return self.salary

    def calculate_bonus(self):
        return 0.02 * self.salary
    
    def calculate_total_salary(self):
        return self.calculate_salary() + self.calculate_bonus() + 2000


class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def calculate_bonus(self):
        return 0.01 * self.hourly_rate * self.hours_worked


class ContractorEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked, bonus):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.bonus = bonus

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def calculate_bonus(self):
        return self.bonus


if __name__ == "__main__":
    full_time_employee = FullTimeEmployee("John Doe", 5000)
    part_time_employee = PartTimeEmployee("Jane Doe", 20, 40)
    contractor_employee = ContractorEmployee("Jack Doe", 25, 40, 1000)

    print(f"{full_time_employee.name}: {full_time_employee.calculate_total_salary()}")
    print(f"{part_time_employee.name}: {part_time_employee.calculate_total_salary()}")
    print(f"{contractor_employee.name}: {contractor_employee.calculate_total_salary()}")