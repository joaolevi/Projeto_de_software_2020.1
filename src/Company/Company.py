class Company:
    def __init__(self, Employees, name, bankID, agency, account):
        self.__employeesList = [Employees]
        self.__name = name
        self.__bankID = bankID
        self.__agency = agency
        self.__account = account

    def get_employees(self):
        return self.__employeesList
    def set_employeesList(self, new_employeesList):
        self.__employeesList = new_employeesList
    
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name
    
    def get_bankID(self):
        return self.__bankID
    def set_bankID(self, new_bankID):
        self.__bankID = new_bankID
    
    def get_agency(self):
        return self.__agency
    def set_agency(self, new_agency):
        self.__agency = new_agency
    
    def get_account(self):
        return self.__account
    def set_account(self, new_account):
        self.__account = new_account

    def add_employee(self, new_employee):
        self.__employeesList.append(new_employee)