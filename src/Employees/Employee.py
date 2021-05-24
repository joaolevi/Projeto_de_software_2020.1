class Employee:
    def __init__(self, name, rg, id, adress, sindMember, paymentMethod, date):
        self.name = name
        self.rg = rg
        self.adress = adress
        self.sindMember = sindMember
        self.id = id
        self.sind_id = None
        self.bankAcc = None
        self.paymentMethod = paymentMethod
        self.tax_value = 0
        self.workHours = []
        self.payDate = None
        self.last_pay_date = date

    def get_name(self): return self.name
    def set_name(self, name):
        self.name = name

    def get_adress(self): return self.adress
    def set_adress(self, new_adress): self.adress = new_adress

    def get_rg(self):
        return self.rg
    def set_rg(self, new_rg):
        self.rg = new_rg

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

    def get_paymentMethod(self):
        return self.paymentMethod
    def set_paymentMethod(self, new_payMethod):
        self.paymentMethod = new_payMethod
    
    def get_bankAcc(self):
        return self.bankAcc
    def set_bankAcc(self, new_bankAcc):
        self.bankAcc = new_bankAcc

    def get_payDate(self):
        return self.payDate
    def set_payDate(self, new_payDate):
        self.payDate = new_payDate

    def get_last_pay_date(self):
        return self.last_pay_date
    def set_last_pay_date(self, new_date):
        self.last_pay_date = new_date

    def __repr__(self):
        return "%s, %s\n" %(self.name, self.id)