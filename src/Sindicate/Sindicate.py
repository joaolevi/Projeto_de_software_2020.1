class Sidicate:
    def __init__(self, members, taxPerMonth, serviceTax):
        self.__membersList = [members]
        self.__taxPerMonth = taxPerMonth
        self.__serviceTax = serviceTax

    def get_membersList(self):
        return self.__membersList
    def set_membersList(self, new_list):
        self.__membersList = new_list
    
    def get_taxPerMonth(self):
        return self.__taxPerMonth
    def set_taxPerMonth(self, new_taxPerMonth):
        self.__taxPerMonth = new_taxPerMonth
    
    def get_serviceTax(self):
        return self.__serviceTax
    def set_serviceTax(self, new_serviceTax):
        self.__serviceTax = new_serviceTax