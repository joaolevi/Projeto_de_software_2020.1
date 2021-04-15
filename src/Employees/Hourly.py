from Employees.Employee import Employee

class Hourly(Employee):
    def __init__(self, name, adress, sindMember, workHours):
        super().__init__(name, adress, sindMember)
        self.__workHours = workHours

    def get_workHours(self):
        return self.__workHours
    def set_workHours(self, hours):
        self.__workHours += hours
    
