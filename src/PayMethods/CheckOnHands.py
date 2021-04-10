from src.PayMethods import PayMethod

class CheckOnHands(PayMethod):
    def __init__(self, value, date, companyBankID, companyAgency, companyAccount, checkNum):
        super.__init__(value, date)
        self.__companyBankID: companyBankID
        self.__companyAgency: companyAgency
        self.__companyAccount: companyAccount
        self.__checkNum: checkNum
    
    def get_companyBankID(self):
        return self.__companyAccount
    def set_companyBankID(self, new_bankID):
        self.__companyBankID = new_bankID
    
    def get_companyAgency(self):
        return self.__companyAgency
    def set_companyAgency(self, new_companyAgency):
        self.__companyAgency = new_companyAgency
    
    def get_companyAccount(self):
        return self.__companyAccount
    def set_companyAccount(self, new_companyAccount):
        self.__companyAccount = new_companyAccount
    
    def get_checkNum(self):
        return self.__checkNum
    def set_checkNum(self, new_checkNum):
        self.__checkNum = new_checkNum
    
