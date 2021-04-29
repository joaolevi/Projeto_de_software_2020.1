from Company.Company import Company
import json
import os

datapath = os.path.join("Projeto_de_software_2020.1", "")

f = open('/home/levi/Documentos/p3/Projeto_de_software_2020.1/employees.json')
data = json.load(f)

parqueShopping = Company("Parque Shopping", "001", "3021-2", "45021-1")

for emp in data:
    parqueShopping.add_employee(emp['nome'], emp['rg'], emp['endereco'], emp['sindMember'], emp['emp_type'],
                                emp['payMethod'], emp['date'], emp['wage'], emp['hour_value'],
                                bankAcc={'bankID':emp['bankID'], 'agency':emp['agency'], 'account':emp['account']})
print(parqueShopping.employeesList)
f.close()


