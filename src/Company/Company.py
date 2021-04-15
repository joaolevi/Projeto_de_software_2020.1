import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from Employees.Hourly import Hourly
from Employees.Comissioned import Comissioned
from Employees.Salaried import Salaried
from TimeRegister.TimeRegister import TimeRegister
from BankDatas.BankData import BankData

class Company(BankData):
    def __init__(self, company_name, bankID, agency, account):
        super().__init__(bankID, agency, account)
        self.__employeesList = []
        self.company_name = company_name

    def get_employeesList(self):
        return self.__employeesList
    def set_employeesList(self, new_employeesList):
        self.__employeesList = new_employeesList
    
    def get_company_name(self):
        return self.company_name
    def set_name(self, new_name):
        self.company_name = new_name

    def get_employee(self, emp_id):
        for w in self.__employeesList:
            print(w.id)
            if w.id == emp_id:
                return w

    def add_employee(self, name, rg, id, adress, sindMember, emp_type, wage=None):
        new_id = int(rg[:-3])*27
        if emp_type == "Comissioned":
            emp = Comissioned(name=name, rg=rg, id=new_id, adress=adress, sindMember=sindMember, wage=wage, comission=0)
        elif emp_type == "Salaried":
            emp = Salaried(name=name, rg=rg, id=new_id, adress=adress, sindMember=sindMember, wage=wage)
        elif emp_type == "Hourly":
            emp = Hourly(name=name, rg=rg, id=new_id, adress=adress, sindMember=sindMember, workHours=0)

        self.__employeesList.append(emp)

    def remove_employee(self, worker_name):
        for w in self.__employeesList:
            if w.name == worker_name:
                self.__employeesList.remove(w)

    def timeRegister(self, emp_id, date, workHours):
        t = TimeRegister(date, workHours)
        e = self.get_employee(emp_id)
        if e.id == emp_id:
            self.__employeesList[e].add_timeRegister(t)
    


parqueShopping = Company("Parque Shopping", "001", "3021-2", "45021-1")
parqueShopping.add_employee(name="João Levi Gomes de Lima", rg="35913738", id="123", adress="R. Alameda Slim", 
                            sindMember=False, emp_type="Salaried", wage=23054.4)
parqueShopping.add_employee(name="Pedro Igor Gomes", rg="123456", id="12345", adress="R. Hotel Jatiuca",
                            sindMember=True, emp_type="Hourly")
print(parqueShopping.get_employeesList())
parqueShopping.timeRegister(969651, "01-10-2021", 8)
e = parqueShopping.get_employee(969651)
print(e.get_timeRegister())

