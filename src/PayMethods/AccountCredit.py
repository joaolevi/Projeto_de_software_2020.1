import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from PayMethods.PayMethod import PayMethod
from BankDatas.BankData import BankData

class AccountCredit(PayMethod, BankData):
    def __init__(self, value, date, bankID, accountNum, agencyNum):
        PayMethod.__init__(self, value, date)
        BankData.__init__(self, bankID, accountNum, agencyNum)