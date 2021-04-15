import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from Employees.Hourly import Hourly
from Employees.Comissioned import Comissioned
from Employees.Salaried import Salaried
from TimeRegister.TimeRegister import TimeRegister
from Sales.Sales import Sales
from BankDatas.BankData import BankData

class Company(BankData):
    def __init__(self, company_name, bankID, agency, account):
        super().__init__(bankID, agency, account)
        self.employeesList = []
        self.company_name = company_name
        self.employeesTimeRegister = []
        self.sales= []

    def get_employeesList(self):
        return self.employeesList
    def set_employeesList(self, new_employeesList):
        self.employeesList = new_employeesList
    
    def get_company_name(self):
        return self.company_name
    def set_name(self, new_name):
        self.company_name = new_name

    def get_employee(self, emp_id):
        x = 0
        while x < len(self.employeesList):
            if self.employeesList[x].id == emp_id:
                return x
            else:
                x+=1

    def add_employee(self, name, rg, id, adress, sindMember, emp_type, wage=None):
        new_id = int(rg[:-3])*27
        if emp_type == "Comissioned":
            emp = Comissioned(name=name, rg=rg, id=new_id, adress=adress, sindMember=sindMember, wage=wage)
        elif emp_type == "Salaried":
            emp = Salaried(name=name, rg=rg, id=new_id, adress=adress, sindMember=sindMember, wage=wage)
        elif emp_type == "Hourly":
            emp = Hourly(name=name, rg=rg, id=new_id, adress=adress, sindMember=sindMember)

        self.employeesList.append(emp)

    def remove_employee(self, emp_id):
        i = self.get_employee(emp_id)
        self.employeesList.remove(i)

    def timeRegister(self, emp_id, date, workHours):
        t = TimeRegister(date, workHours)
        e = self.get_employee(emp_id)
        emp = self.employeesList[e]
        emp.add_workHours(t)
        self.employeesTimeRegister.append({"Employee": emp, "Date": date, "WorkHours": workHours})

    def set_sale_to_employee(self, emp_id, date, value):
        i = self.get_employee(emp_id)
        emp = self.employeesList[i]
        s = Sales(date=date, value=value, seller=emp)
        try:
            emp.add_comission(s.get_comission())
            self.sales.append(s)
        except AttributeError:
            print("ERRO: Empregado não é do tipo Comissionado")


### Teste de empregados
parqueShopping = Company("Parque Shopping", "001", "3021-2", "45021-1")
parqueShopping.add_employee(name="João Levi Gomes de Lima", rg="35913738", id="123", adress="R. Alameda Slim", 
                            sindMember=False, emp_type="Comissioned", wage=23054.4)
parqueShopping.add_employee(name="Pedro Igor Gomes", rg="123456", id="12345", adress="R. Hotel Jatiuca",
                            sindMember=True, emp_type="Hourly")

### Teste de registro de ponto                          
# print(parqueShopping.get_employeesList())
# parqueShopping.timeRegister(3321, "01-10-2021", 8)
# parqueShopping.timeRegister(3321, "01-12-2021", 10)
# parqueShopping.timeRegister(3321, "01-13-2021", 9)
# parqueShopping.timeRegister(3321, "01-14-2021", 8)
# e = parqueShopping.get_employee(3321)
# print(parqueShopping.employeesList[e].workHours)
# print(parqueShopping.employeesTimeRegister)

### Teste de comissão
# parqueShopping.set_sale_to_employee(969651, "10-2-2021", 350.56)
# parqueShopping.set_sale_to_employee(969651, "10-2-2021", 231.22)
# parqueShopping.set_sale_to_employee(969651, "10-2-2021", 111)
# outro = parqueShopping.get_employee(969651)
# print(parqueShopping.employeesList[outro].get_comission())
# print(parqueShopping.sales)

