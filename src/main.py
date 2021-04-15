from Employees.Employee import Employee
from Company.Company import Company

emp1 = Employee("João", "10231023", "2130120301", False)
emp2 = Employee("Levi", "120230", "1299212", True)

parqueShopping = Company("Parque Shopping Maceió", "001", "35102-5", "2302-1")

parqueShopping.add_employee(emp1)
parqueShopping.add_employee(emp2)
empList = parqueShopping.get_employees()
print(empList)