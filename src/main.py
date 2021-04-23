from Company.Company import Company


parqueShopping = Company("Parque Shopping", "001", "3021-2", "45021-1")
parqueShopping.add_employee(name="João Levi Gomes de Lima", rg="35913738", adress="R. Alameda Slim", 
                            sindMember=False, emp_type="Hourly", payMethod="AccountCredit", date='2021-4-10', 
                            bankAcc={'bankID':"001", 'agency':"41730-0", 'account':'37501-0'}, hour_value=123.4)

parqueShopping.add_employee(name="Pedro Igor Gomes", rg="123456", adress="R. Hotel Jatiuca",
                            sindMember=True, payMethod='CheckOnHands',emp_type="Hourly", date='2021-4-1', hour_value=354)
# print(parqueShopping.employeesList)

parqueShopping.pay_employees("2021-05-26")
# print(parqueShopping.payment_register)