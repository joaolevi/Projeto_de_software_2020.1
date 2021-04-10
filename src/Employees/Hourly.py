from src.Employees import Employee

class Salaried(Employee):
    def __init__(self, name, CPF, RG, workHours, sindMember):
        super().__init(name, CPF, RG, sindMember)
        self.__workHours = workHours

    def get_workHours(self):
        return self.__workHours
    def set_workHours(self, hours):
        self.__workHours += hours
    

