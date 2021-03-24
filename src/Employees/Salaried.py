from src import Employee

class Salaried(Employee):
    def __init__(self, name, CPF, RG, wage):
        super().__init(name, CPF, RG)
        self.__wage = wage

    def get_wage(self):
        return self.__wage
    def set_wage(self, value):
        self.__wage = value

    