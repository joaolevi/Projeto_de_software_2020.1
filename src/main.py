from Company.Company import Company


parqueShopping = Company("Parque Shopping", "001", "3021-2", "45021-1")
parqueShopping.add_employee(name="João Levi Gomes de Lima", rg="35913738", adress="R. Alameda Slim", 
                            sindMember=False, emp_type="Salaried", wage=4523.37, payMethod="DeliveryCheck", date='2021-3-10', 
                            hour_value=43.44)

parqueShopping.add_employee(name="Pedro Igor Gomes", rg="123456", adress="R. Hotel Jatiuca",
                            sindMember=True, payMethod='AccountCredit',emp_type="Hourly", 
                            date='2021-4-1', hour_value=35.27,
                            bankAcc={'bankID':'002', 'agency':'4510-1', 'account':'23041-2'})
# print(parqueShopping.employeesList)

parqueShopping.pay_employees("2021-04-30")
# print(parqueShopping.payment_register)

print(parqueShopping.payment_register)