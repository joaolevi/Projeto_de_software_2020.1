from Employees.Employee import Employee

class Salaried(Employee):
    def __init__(self, name, rg, id, adress, sindMember, wage, paymentMethod, hiring_date):
        super().__init__(name, rg, id, adress, sindMember, paymentMethod, hiring_date)
        self.__wage = wage
        self.payDate = "monthly-$"

    def get_wage(self):
        return self.__wage
    def set_wage(self, value):
        self.__wage = value


# e = Salaried("João Levi", "00231023", "19231293", 6559, False)
# print(e)