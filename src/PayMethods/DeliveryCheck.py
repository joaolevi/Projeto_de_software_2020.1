import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from PayMethods.CheckOnHands import CheckOnHands

class DeliveryCheck(CheckOnHands):
    def __init__(self, value, date, bankID, companyAgency, companyAccount):
        super().__init__(value, date, bankID, companyAgency, companyAccount)
        self.__adress: None
    
    def get_adress(self):
        return self.__adress
    def set_adress(self, new_adress):
        self.__adress = new_adress

# d = DeliveryCheck(123, "10-1-2021", "001", "2030-1", "129239-1")
# print(d.set_adress( "Ali na casa"))
# print(d.get_adress())