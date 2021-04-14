from Tax import Tax

class ServiceTax(Tax):
    def __init__(self, value, service_name):
        super().__init__(value)
        self.__service_name = service_name
    
    def get_service_name(self):
        return self.__service_name
    def set_service_name(self, new_service_name):
        self.__service_name = new_service_name