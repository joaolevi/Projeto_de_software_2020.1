from Employee import Employee

class Salaried(Employee):
    def __init__(self, name, CPF, RG, wage, sindMember):
        super().__init__(name, CPF, RG, sindMember)
        self.__wage = wage

    def get_wage(self):
        return self.__wage
    def set_wage(self, value):
        self.__wage = value


# e = Salaried("João Levi", "00231023", "19231293", 6559, False)
# print(e)