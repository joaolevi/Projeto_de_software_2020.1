class Employee:
    def __init__(self, name, CPF, RG):
        self.__name = name
        self.__cpf = CPF
        self.__rg = RG

    def get_name(self): return self.__name
    def set_name(self, name): self.__name = name

    def get_cpf(self): return self.__cpf
    def set_cpf(self, cpf): self.__cpf = cpf

    def get_rg(self): return self.__rg
    def set_rg(self, rg): self.__rg = rg



