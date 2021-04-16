from Employees.Employee import Employee

class Hourly(Employee):
    def __init__(self, name, rg, id, adress, sindMember, paymentMethod):
        super().__init__(name, rg, id, adress, sindMember, paymentMethod)
        self.__workHours = -1

    def get_workHours(self):
        return self.__workHours
    def set_workHours(self, hours):
        self.__workHours += hours
    
