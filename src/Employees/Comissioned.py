from Employees.Employee import Employee

class Comissioned(Employee):
    def __init__(self, name, rg, id, adress, sindMember, wage, paymentMethod, hiring_date):
        super().__init__(name, rg, id, adress, sindMember, paymentMethod, hiring_date)
        self.__wage = wage
        self.__comission = 0
        self.payDate = "weekly-2-friday"

    def get_wage(self):
        return self.__wage
    def set_wage(self, wage):
        self.__wage = wage

    def get_comission(self):
        return self.__comission
    
    def add_comission(self, comission):
        self.__comission += comission

    def clear_comission(self):
        self.__comission = 0
    