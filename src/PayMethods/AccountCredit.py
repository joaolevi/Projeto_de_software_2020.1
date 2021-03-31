from src import PayMethod

class AccountCredit(PayMethod):
    def __init__(self, value, date, bankID, accountNum, agencyAccount):
        super.__init__(value, date)
        self.__bankID: bankID
        self.__accountNum: accountNum
        self.__agencyAccount: agencyAccount