class TimeRegister:
    def __init__(self, name, date, hours):
        self.__name = name
        self.__date = date
        self.__hours = hours

    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name

    def get_date(self):
        return self.__date
    def set_date(self, new_date):
        self.__date = new_date
    
    def get_hours(self):
        return self.__hours
    def set_hours(self, new_hours):
        self.__hours = new_hours