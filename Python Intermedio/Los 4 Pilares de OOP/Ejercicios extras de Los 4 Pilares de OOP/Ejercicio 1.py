

class Employee():
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
        pass

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary   

    @salary.setter
    def salary(self, valor):
        if valor < 0:
            print("The salary can not be negative")
        else: 
            self._salary = valor

    def promote(self, promote):
        self.salary = (promote*self.salary)+self.salary

employee = Employee("Ana", 1000)
employee.promote(0.1)  # +10%
print(employee.salary)