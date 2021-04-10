class BankData:
    def __init__(self, bankID, agency, account):
        self.__bankID = bankID
        self.__agency = agency
        self.__account = account
    
    def get_bankID(self):
        return self.__bankID
    def set_bankID(self, new_bankID):
        self.__bankID = new_bankID
    
    def get_agency(self):
        return self.__agency
    def set_agency(self, new_agency):
        self.__agency = new_agency
    
    def get_account(self):
        return self.__account
    def set_account(self, new_account):
        self.__account = new_account