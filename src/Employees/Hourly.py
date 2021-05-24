from Employees.Employee import Employee

class Hourly(Employee):
    def __init__(self, name, rg, id, adress, sindMember, paymentMethod, date, hour_value):
        super().__init__(name, rg, id, adress, sindMember, paymentMethod, date)
        self.workHours = []
        self.hour_value = hour_value
        self.payDate = "weekly-1-friday"

    def get_workHours(self):
        return self.workHours
    def set_workHours(self, hours):
        self.workHours += hours
    
