class Employee:
    def __init__(self, name, rg, id, adress, sindMember):
        self.name = name
        self.__rg = rg
        self.__adress = adress
        self.sindMember = sindMember
        self.id = id
        self.tax_value = 0
        self.workHours = []

    def get_name(self): return self.__name
    def set_name(self, name): self.__name = name

    def get_adress(self): return self.__adress
    def set_adress(self, new_adress): self.__adress = new_adress

    def get_rg(self):
        return self.__rg
    def set_rg(self, new_rg):
        self.__rg = new_rg

    def get_sindMember(self):
        return self.sindMember
    def set_sindMember(self):
        self.sindMember = not(self.sindMember)
        
    def get_workHours(self):
        return self.workHours
    
    def add_workHours(self, timeReg):
        self.workHours.append(timeReg)
    
    def clear_workHours(self):
        self.workHours = None

    def __repr__(self):
        return "%s\n" %(self.name)