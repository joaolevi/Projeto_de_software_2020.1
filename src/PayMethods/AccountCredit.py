import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from PayMethods.PayMethod import PayMethod
from BankDatas.BankData import BankData

class AccountCredit(PayMethod, BankData):
    def __init__(self, value, date, bankID, accountNum, agencyNum, name):
        PayMethod.__init__(self, value, date)
        BankData.__init__(self, bankID, accountNum, agencyNum)
        self.name = name
    
    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name

    def __repr__(self):
        rep = super(AccountCredit, self).__repr__()
        return "%s, %r\n" %(self.name, rep)

# a = AccountCredit(2031.2, "2021-02-01", "001", "32021-01", "2320-1", "João")
# print(a)