class Employee:
    def __init__(self, name, emp_type, pay_method, CPF, RG, adress, pis, agency, account, bank):
        self.__name = name
        self.__employed_type = emp_type
        self.__pay_method = pay_method
        self.__cpf = CPF
        self.__rg = RG
        self.__adress = adress
        self.__pis = pis
        self.__id = None
        self.__bank_acc = {"agency":agency, "account":account, "bank":bank}
        self.__sindicate_member = False
        self.__sindicateID = None
        self.__wage = 0
        self.__service_tax = 0
        self.__sindTax = 0
    
    def __repr__(self):
        return "%s %s \n%s %s %s" %(self.__name, self.__adress, self.__cpf, self.__rg, self.__employed_type)

    def get_name(self): return self.__name
    def set_name(self, name): self.__name = name
        
    def get_employed_type(self): return self.__employed_type
    def set_employed_type(self, employed_type): self.__employed_type = employed_type

    def get_pay_method(self): return self.__pay_method
    def set_pay_method(self, pay_method): self.__pay_method = pay_method

    def get_cpf(self): return self.__cpf
    def set_cpf(self, cpf): self.__cpf = cpf

    def get_rg(self): return self.__rg
    def set_rg(self, rg): self.__rg = rg

    def get_adress(self): return self.__adress
    def set_adress(self, adress): self.__adress = adress

    def get_pis(self): return self.__pis
    def set_pis(self, pis): self.__pis = pis

    def get_id(self): return self.__id
    def set_id(self):
        if self.__id == None:
            num = int(int(self.__rg)/253)
            self.__id = num

    def get_sindicate_member(self): return self.__sindicate_member
    def set_sindicate_member(self): self.__sindicate_member = not(self.__sindicate_member)

    def get_sindicateID(self): 
        if self.__sindicate_member: return self.__sindicateID
    def set_sindicateID(self):
        if self.__sindicate_member:
            sidID = int(int(self.__cpf)/253)
            self.__sindicateID = sidID

    def get_wage(self): return self.__wage
    def set_wage(self, value): self.__wage += value

    def get_service_tax(self): return self.__service_tax
    def set_service_tax(self, value): self.__service_tax += value

    def get_sindTax(self): return self.__sindTax
    def set_sindTax(self):
        if not(self.__sindTax & self.__sindicate_member):
            if self.__employed_type == "hourly":
                self.__sindTax = float(self.__wage*3/100)
            elif self.__employed_type == "salaried":
                self.__sindTax = float(self.__wage*5/100)
            elif self.__employed_type == "commissioned":
                self.__sindTax = float(self._wage*6/100)
    
    def get_bank_acc(self): return self.__bank_acc
    def set_bank_acc(self, agency, account, bank):
        self.__bank_acc = {"agency": agency, "account": account, "bank": bank}



new = Employed(name="João Levi", adress="R. Helena Costa tenório", 
                emp_type="hourly", pay_method="contracheque", CPF="08666271469", 
                RG="35913738", pis="65132135", agency="3057-0", account="41730-0", bank="001")




