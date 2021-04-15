class Employee:
    def __init__(self, name, rg, id, adress, sindMember):
        self.name = name
        self.__rg = rg
        self.__adress = adress
        self.__sindMember = sindMember
        self.id = id
        self.timeRegister = []

    def get_name(self): return self.__name
    def set_name(self, name): self.__name = name

    def get_adress(self): return self.__adress
    def set_adress(self, new_adress): self.__adress = new_adress

    def get_rg(self):
        return self.__rg
    def set_rg(self, new_rg):
        self.__rg = new_rg

    def get_sindMember(self):
        return self.__sindMember
    def set_sindMember(self):
        self.__sindMember = not(self.__sindMember)
        
    def get_timeRegister(self):
        return self.timeRegister
    
    def add_timeRegister(self, timeReg):
        self.timeRegister.append(timeReg)
    
    def clear_timeRegister(self):
        self.timeRegister = None

    def __repr__(self):
        return "%s\n" %(self.name)