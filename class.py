class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self) -> float:
        return float(self.salary)

class EmployeeCLT (Employee):
    def __init__(self, name, salary, benefits):
        super().__init__(name, salary)
        self.benefits = benefits

    def get_salary(self) -> float:
        return float(self.salary + self.benefits)

class PayRoll:
    def __init__(self, employees):
        self.employees = employees

    def calculate(self):
        pays = []
        total = 0

        for employee in self.employees:
            employee_salary = employee.get_salary()

            pays.append({ "name": employee.name, "salary": employee_salary })
            total += employee_salary

        return { "pays": pays, "total": total }
    
lucas = Employee('Lucas', 9000)
bianca = EmployeeCLT('Bianca', 1980, 500)
marcos = EmployeeCLT('Marcos', 9500, 750)

pay_roll = PayRoll([lucas, bianca, marcos])

pay_roll_result = pay_roll.calculate()

print(pay_roll_result)

print("\nEmployees salaries: ")

for pay in pay_roll_result['pays']:
    print(f"{pay['name']}: R$ {pay['salary']}")

print(f"\nTotal: R$ {pay_roll_result['total']}")