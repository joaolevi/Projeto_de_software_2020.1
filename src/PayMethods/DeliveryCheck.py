from src.PayMethods import CheckOnHands

class DeliveryCheck(CheckOnHands):
    def __init__(self, value, date, adress, bankID, companyAgency, companyAccount, checkNum):
        super.__init__(value, date, bankID, companyAgency, companyAccount, checkNum)
        self.__adress: adress
    
    def get_adress(self):
        return self.__adress
    def set_adress(self, new_adress):
        self.__adress = new_adress