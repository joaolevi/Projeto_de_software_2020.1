from src import PayMethod

class CheckOnHands(PayMethod):
    def __init__(self, value, date, bankID, companyAgency, companyAccount, checkNum):
        super.__init__(value, date)
        self.__bankID: bankID
        self.__companyAgency: companyAgency
        self.__companyAccount: companyAccount
        self.__checkNum: checkNum