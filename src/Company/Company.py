import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from Employees.Hourly import Hourly
from Employees.Comissioned import Comissioned
from Employees.Salaried import Salaried
from BankDatas.BankData import BankData

class Company(BankData):
    def __init__(self, company_name, bankID, agency, account):
        super().__init__(bankID, agency, account)
        self.__employeesList = []
        self.company_name = company_name

    def get_employees(self):
        return self.__employeesList
    def set_employeesList(self, new_employeesList):
        self.__employeesList = new_employeesList
    
    def get_company_name(self):
        return self.company_name
    def set_name(self, new_name):
        self.company_name = new_name

    def add_employee(self, name, adress, sindMember, emp_type, wage=None):
        if emp_type == "Comissioned":
            emp = Comissioned(name=name, adress=adress, sindMember=sindMember, wage=wage, comission=0)
        elif emp_type == "Salaried":
            emp = Salaried(name=name, adress=adress, sindMember=sindMember, wage=wage)
        else:
            emp = Hourly(name=name, adress=adress, sindMember=sindMember, workHours=0)

        self.__employeesList.append(emp)

    def remove_employee(self, worker_name):
        for w in self.__employeesList:
            if w.name == worker_name:
                self.__employeesList.remove(w)

parqueShopping = Company("Parque Shopping", "001", "3021-2", "45021-1")
print(parqueShopping.get_employees())
parqueShopping.add_employee("João Levi Gomes de Lima", "R. Alameda Slim", False, "Salaried", wage=23054.4)
print(parqueShopping.get_employees())