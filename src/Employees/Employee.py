class Employee:
    def __init__(self, name, adress, sindMember):
        self.name = name
        self.__adress = adress
        self.__sindMember = sindMember

    def get_name(self): return self.__name
    def set_name(self, name): self.__name = name

    def get_adress(self): return self.__adress
    def set_adress(self, new_adress): self.__adress = new_adress

    def get_sindMember(self):
        return self.__sindMember
    def set_sindMember(self):
        self.__sindMember = not(self.__sindMember)

    def __repr__(self):
        return "%s\n" %(self.__name)