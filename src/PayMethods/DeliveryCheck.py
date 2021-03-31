from src.PayMethods import PayMethod

class DeliveryCheck(PayMethod):
    def __init__(self, value, date, adress, bankID, companyAgency, companyAccount, checkNum):
        super.__init__(value, date)
        self.__adress: adress
        self.__bankID: bankID
        self.__companyAgency: companyAgency
        self.__companyAccount: companyAccount
        self.__checkNum: checkNum