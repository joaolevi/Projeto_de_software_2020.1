from Employees.Employee import Employee

class Comissioned(Employee):
    def __init__(self, name, adress, sindMember, wage, comission, ):
        super().__init__(name, adress, sindMember)
        self.__wage = wage
        self.__comission = comission

    def get_wage(self):
        return self.__wage
    def set_wage(self, wage):
        self.__wage = wage

    def get_comission(self):
        return self.__comission
    def set_comission(self, comission):
        self.__comission = comission