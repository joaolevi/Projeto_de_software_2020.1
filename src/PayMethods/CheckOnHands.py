import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from BankDatas.BankData import BankData
from PayMethod import PayMethod

class CheckOnHands(PayMethod, BankData):
    def __init__(self, value, date, companyBankID, companyAgency, companyAccount, checkNum):
        PayMethod.__init__(self, value, date)
        BankData.__init__(self, companyBankID, companyAgency, companyAccount)
        self.__checkNum: checkNum
    
    def get_checkNum(self):
        return self.__checkNum
    def set_checkNum(self, new_checkNum):
        self.__checkNum = new_checkNum
