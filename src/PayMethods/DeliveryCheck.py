import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from PayMethods.CheckOnHands import CheckOnHands

class DeliveryCheck(CheckOnHands):
    def __init__(self, name, value, date, bankID, companyAgency, companyAccount, check_num, adress):
        super().__init__(name, value, date, bankID, companyAgency, companyAccount, check_num)
        self.adress: None
    
    def get_adress(self):
        return self.adress
    def set_adress(self, new_adress):
        self.adress = new_adress

# d = DeliveryCheck(123, "10-1-2021", "001", "2030-1", "129239-1")
# print(d.set_adress( "Ali na casa"))
# print(d.get_adress())