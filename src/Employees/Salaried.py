from src.Employees import Employee

class Salaried(Employee):
    def __init__(self, name, CPF, RG, wage, sindMember):
        super().__init(name, CPF, RG, sindMember)
        self.__wage = wage

    def get_wage(self):
        return self.__wage
    def set_wage(self, value):
        self.__wage = value

    