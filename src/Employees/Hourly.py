from Employees.Employee import Employee

class Hourly(Employee):
    def __init__(self, name, rg, id, adress, sindMember, paymentMethod, date):
        super().__init__(name, rg, id, adress, sindMember, paymentMethod, date)
        self.workHours = -1
        self.payDate = "weekly-1-friday"

    def get_workHours(self):
        return self.workHours
    def set_workHours(self, hours):
        self.workHours += hours
    
