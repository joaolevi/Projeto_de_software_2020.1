from Employees.Employee import Employee

class Comissioned(Employee):
    def __init__(self, name, rg, id, adress, sindMember, wage, paymentMethod, date):
        super().__init__(name, rg, id, adress, sindMember, paymentMethod, date)
        self.wage = wage
        self.comission = 0
        self.payDate = "weekly-2-friday"

    def get_wage(self):
        return self.wage
    def set_wage(self, wage):
        self.wage = wage

    def get_comission(self):
        return self.comission
    
    def add_comission(self, comission):
        self.comission += comission

    def clear_comission(self):
        self.comission = 0
    