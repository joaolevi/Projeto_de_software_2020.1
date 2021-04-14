from Employee import Employee

class Hourly(Employee):
    def __init__(self, name, CPF, RG, sindMember, workHours):
        super().__init__(name, CPF, RG, sindMember)
        self.__workHours = workHours

    def get_workHours(self):
        return self.__workHours
    def set_workHours(self, hours):
        self.__workHours += hours
    
e = Hourly("João Levi", "00231023", "19231293", False, 23034)
print(e)
