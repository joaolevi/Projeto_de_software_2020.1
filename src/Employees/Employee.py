class Employee:
    def __init__(self, name, CPF, RG, sindMember):
        self.__name = name
        self.__cpf = CPF
        self.__rg = RG
        self.__sindMember = sindMember

    def get_name(self): return self.__name
    def set_name(self, name): self.__name = name

    def get_cpf(self): return self.__cpf
    def set_cpf(self, cpf): self.__cpf = cpf

    def get_rg(self): return self.__rg
    def set_rg(self, rg): self.__rg = rg

    def get_sindMember(self):
        return self.__sindMember
    def set_sindMember(self):
        self.__sindMember = not(self.__sindMember)

    def __repr__(self):
        return "%s\n%s\n%s\n" %(self.__name, self.__cpf, self.__rg)

emp = Employee("João Levi", "08666271469", "35913738", True)
print(emp)
