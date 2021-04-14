from PayMethod import PayMethod

class AccountCredit(PayMethod):
    def __init__(self, value, date, bankID, accountNum, agencyAccount):
        super().__init__(value, date)
        self.__bankID: bankID
        self.__accountNum: accountNum
        self.__agencyAccount: agencyAccount

    def get_bankID(self):
        return self.__bankID
    def set_bankID(self, new_bankID):
        self.__bankID = new_bankID
    
    def get_accountNum(self):
        return self.__accountNum
    def set_accountNum(self, new_accountNum):
        self.__accountNum = new_accountNum
    
    def get_agencyAccount(self):
        return self.__agencyAccount
    def set_agencyAccount(self, new_agencyAccount):
        self.__agencyAccount = new_agencyAccount