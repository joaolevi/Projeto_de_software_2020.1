import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from PayMethods.PayMethod import PayMethod
from BankDatas.BankData import BankData

class AccountCredit(PayMethod, BankData):
    def __init__(self, name, value, date, bankID, accountNum, agencyNum):
        PayMethod.__init__(self, name, value, date)
        BankData.__init__(self, bankID, accountNum, agencyNum)
        self.name = name
    
    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name

    def __repr__(self):
        rep = PayMethod(self.name, self.value, self.date).__repr__()
        return "%r, %s" %(rep, self.__class__.__name__)

# a = AccountCredit(2031.2, "2021-02-01", "001", "32021-01", "2320-1", "João")
# print(a)