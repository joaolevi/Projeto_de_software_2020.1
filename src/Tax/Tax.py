class Tax:
    def __init__(self, value):
        self.__value = value
    
    def get_value(self):
        return self.__value
    def set_value(self, new_value):
        self.__value = new_value