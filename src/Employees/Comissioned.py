from Employees.Employee import Employee

class Comissioned(Employee):
    def __init__(self, name, rg, id, adress, sindMember, wage):
        super().__init__(name, rg, id, adress, sindMember)
        self.__wage = wage
        self.__comission = 0

    def get_wage(self):
        return self.__wage
    def set_wage(self, wage):
        self.__wage = wage

    def get_comission(self):
        return self.__comission
    def set_comission(self, comission):
        self.__comission = comission