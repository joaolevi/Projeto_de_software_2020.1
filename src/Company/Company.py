import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from Employees.Hourly import Hourly
from Employees.Comissioned import Comissioned
from Employees.Salaried import Salaried
from Sindicate.Sindicate import Sindicate
from TimeRegister.TimeRegister import TimeRegister
from Sales.Sales import Sales
from BankDatas.BankData import BankData
from PayMethods.AccountCredit import AccountCredit
from PayMethods.CheckOnHands import CheckOnHands
from PayMethods.DeliveryCheck import DeliveryCheck

class Company(BankData):
    def __init__(self, company_name, bankID, agency, account):
        super().__init__(bankID, agency, account)
        self.employeesList = []
        self.company_name = company_name
        self.employeesTimeRegister = []
        self.sales= []
        self.pay_schedule = ["weekly-1-friday", "weekly-2-friday", "monthly-$"]

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

    def add_employee(self, name, rg, adress, sindMember, emp_type, payMethod, hiring_date, wage=None, bankAcc=None):
        new_id = int(rg[:-3])*27
        if emp_type == "Comissioned":
            emp = Comissioned(name=name, rg=rg, id=new_id, adress=adress, 
                            paymentMethod = payMethod, sindMember=sindMember, hiring_date=hiring_date, wage=wage)
        elif emp_type == "Salaried":
            emp = Salaried(name=name, rg=rg, id=new_id, adress=adress, hiring_date=hiring_date, sindMember=sindMember, 
                            paymentMethod = payMethod, wage=wage)
        elif emp_type == "Hourly":
            emp = Hourly(name=name, rg=rg, id=new_id, adress=adress, hiring_date=hiring_date, sindMember=sindMember,
                         paymentMethod = payMethod)
        if payMethod == "AccountCredit":
            if bankAcc:
                acc = BankData(bankID=bankAcc['bankID'], agency=bankAcc['agency'], account=bankAcc['account'])
                emp.set_bankAcc(acc)
        self.employeesList.append(emp)

    def remove_employee(self, emp_id):
        i = self.get_employee(emp_id)
        emp = self.employeesList[i]
        self.employeesList.remove(emp)

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

    def change_employee_type(self, emp_id, emp_type, wage=None):
        i = self.get_employee(emp_id)
        emp = self.employeesList[i]
        if emp_type:
            self.remove_employee(emp.id)
            self.add_employee(name=emp.name, rg=emp.rg, adress=emp.adress, sindMember=emp.sindMember, emp_type=emp_type, wage=wage, payMethod=emp.paymentMethod, hiring_date=emp.hiring_date)
            index = self.get_employee(emp.id)
            return index

    def change_employee_details(self, emp_id, emp_t=None, name=None, rg=None, adress=None, bankAcc=None, payMethod=None, wage=None):
        i = self.get_employee(emp_id)
        if emp_t:
            i = self.change_employee_type(emp_id, emp_t, wage)
        if name:
            self.employeesList[i].set_name(name)
        if rg:
            self.employeesList[i].set_rg(rg)
        if adress:
            self.employeesList[i].set_adress(adress)
        if bankAcc:
            self.employeesList[i].set_bankAcc(bankAcc)
        if payMethod:
            self.employeesList[i].set_paymentMethod(payMethod)
        if wage and (isinstance(self.employeesList[i], Comissioned) or isinstance(self.employeesList[i], Salaried)):
            self.employeesList[i].set_wage(wage)

    def set_employee_pay_date(self, emp_id):
        i = self.get_employee(emp_id)
        count = 1
        for option in self.pay_schedule:
            print(count,"-", option)
            count += 1
        choose = int(input("Escolha uma data para o pagamento: "))
        self.employeesList[i].set_payDate(self.pay_schedule[choose-1])
    
    def set_new_pay_schedule(self, schedule):
        if isinstance(schedule, list):
            self.pay_schedule = schedule

    ### It needs more dev 
    # def pay_employees(self, today_date):
    #     for emp in self.employeesList:
    #         if emp.last_pay_date:
    #             payMet = emp.paymentMethod.split("-")

            

        


### Teste de empregados
parqueShopping = Company("Parque Shopping", "001", "3021-2", "45021-1")
parqueShopping.add_employee(name="João Levi Gomes de Lima", rg="35913738", adress="R. Alameda Slim", 
                            sindMember=False, emp_type="Comissioned", payMethod="AccountCredit", hiring_date="2020-1-10", 
                            bankAcc={'bankID':"001", 'agency':"41730-0", 'account':'37501-0'}, wage=23054.4)

parqueShopping.add_employee(name="Pedro Igor Gomes", rg="123456", adress="R. Hotel Jatiuca",
                            sindMember=True, payMethod='CheckOnHands',emp_type="Salaried", hiring_date="2021-01-22")

### Teste função de alterar
i = parqueShopping.get_employee(969651)
emp = parqueShopping.employeesList[i]
print(emp.hiring_date)
parqueShopping.change_employee_details(969651, emp_t="Salaried", name="Levizinho", adress="Helena Costa", rg="11111")

### Teste função de data de pagamento
#  
# h = parqueShopping.get_employee(969651)
# emp2 = parqueShopping.employeesList[h]
# print(emp2.get_payDate())
# new_schedule = ["weekly-2-saturday", "weekly-1-monday", "montlhy-7", "montlhy-18"]
# print(parqueShopping.pay_schedule)
# parqueShopping.set_new_pay_schedule(new_schedule)
# print(parqueShopping.pay_schedule)
# parqueShopping.set_employee_pay_date(969651)
# print(emp2.get_payDate())


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

### Teste do sindicato
# s = Sindicate(25.31)
# i = parqueShopping.get_employee(3321)
# emp = parqueShopping.employeesList[i]
# print(parqueShopping.employeesList[i].tax_value)
# s.month_tax_roll(parqueShopping.employeesList)
# print(parqueShopping.employeesList[i].tax_value)
# s.tax_associator(emp, 'Medical')
# print(parqueShopping.employeesList[i].tax_value)

