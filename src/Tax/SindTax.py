from Tax import Tax

class SindTax(Tax):
    def __init__(self, value, date):
        super().__init__(value)
        self.__date = date
    
    def get_date(self):
        return self.__date
    def set_date(self, new_date):
        self.__date = new_date