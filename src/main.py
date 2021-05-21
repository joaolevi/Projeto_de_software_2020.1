from Company.Company import Company
from Employees.Comissioned import Comissioned
from Employees.Hourly import Hourly
from Employees.Salaried import Salaried
from PayMethods.PayMethod import PayMethod
from Sindicate.Sindicate import Sindicate
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
# print(parqueShopping.employeesList)
f.close()

while(1):
    print("Escolha uma opção: ")
    print("1 - Adicionar empregado\n2 - Remover empregado\n3 - Lançar um Cartão de Ponto\n4 - Lançar um Resultado Venda\n5 - Lançar uma taxa de serviço\n6 - Alterar detalhes de um empregado\n7 - Rodar a folha de pagamento para hoje\n8 - Agenda de Pagamento\n9 - Criação de Novas Agendas de Pagamento\n\n10 - Sair\n\n")
    op = int(input("Escolha: "))
    if op == 10:
        break
    elif op == 1:
        name = input("Nome: ")
        rg = input("Rg: ")
        adress = input("Endereço: ")
        sindMember = input("Membro do sindicato? Se sim digite 1, se não 0")
        print("Tipo de empregado: \n")
        print("1 - Comissionado\n2 - Horista\n3 - Salariado")
        escolha = int(input("Digite a opção: "))
        if escolha == 1:
            emp_type = "Comissioned"
        elif escolha == 2:
            emp_type = "Hourly"
        else:
            emp_type = "Salaried"
        print("Metodo de pagamento: \n")
        print("1 - Crédito em Conta\n2 - Cheque em mãos\n3 - Cheque via correios\n")
        escolha = int(input("Metodo escolhido: "))
        if escolha == 1:
            payMethod = "AccountCredit"
        elif escolha == 2:
            payMethod = "CheckOnHands"
        else:
            payMethod = "DeliveryCheck"
        date = input("Data do contrato: ")
        wage = float(input("Salário: "))
        hour_value = float(input("Hora de trabalho: "))
        print("Dados bancários: ")
        bankID = input("Banco: ")
        agency = input("Agência: ")
        account = input("Conta: ")
        parqueShopping.add_employee(emp['nome'], emp['rg'], emp['endereco'], emp['sindMember'], emp['emp_type'],
                                emp['payMethod'], emp['date'], emp['wage'], emp['hour_value'],
                                bankAcc={'bankID':bankID, 'agency':agency, 'account':account})
        print(parqueShopping.employeesList)



# #Localiza o empregado
# i = parqueShopping.get_employee(11786526)
# #Printa no console o nome e id do empregado selecionado
# print(parqueShopping.employeesList[i], "\n")

# #Lançar um Cartão de Ponto
# parqueShopping.timeRegister(11786526, "2021-05-21", 9)
# parqueShopping.timeRegister(4419495, "2021-05-21", 7)
# print(parqueShopping.employeesTimeRegister,"\n")

# #Lançar um Resultado de Venda
# parqueShopping.set_sale_to_employee(11786526, "2021-05-19", 125.99)
# print(parqueShopping.sales, "\n")

# # Teste do sindicato
# # Cria o sindicato
# s = Sindicate(25.31)
# i = parqueShopping.get_employee(11786526)
# emp = parqueShopping.employeesList[i]
# # Valor atual da taxa que o empregado deve
# print("Taxa:",parqueShopping.employeesList[i].tax_value)
# # Lança a taxa mensal do sindicato nos empregados associados
# s.month_tax_roll(parqueShopping.employeesList)
# print("Taxa:", parqueShopping.employeesList[i].tax_value)
# #Lança uma taxa de serviço específica no empregado selecionado
# s.tax_associator(emp, 'Medical')
# print("Taxa: %.2f" % parqueShopping.employeesList[i].tax_value)

# # Alterar detalhes do empregado
# parqueShopping.change_employee_details(11786526, name="Luana Joana Luisa Moura")
# print(emp)
# print(emp.adress)
# parqueShopping.change_employee_details(11786526, adress="Avenida Jatiuca nº 28")
# print(emp.adress)
# # Altera o tipo de empregado
# print(isinstance(emp, Comissioned))
# parqueShopping.change_employee_details(11786526, "Salaried")
# print(isinstance(emp, Salaried))

# # Rodar a folha de pagamentos para hoje
# parqueShopping.pay_employees("2021-05-21")
# print(parqueShopping.get_payment_register(), "\n")

# #Agenda de pagamento
# h = parqueShopping.get_employee(11786526)
# emp2 = parqueShopping.employeesList[h]
# print("Data de pagamento atual do empregado:", emp2.get_payDate())
# parqueShopping.set_employee_pay_date(11786526)
# print("\nData de pagamento atual do empregado:", emp2.get_payDate(), "\n")

# # Nova agenda de pagamento
# new_schedule = ["weekly-2-saturday", "weekly-1-monday", "montlhy-7", "montlhy-18"]
# print("\nOpções de agenda:", parqueShopping.pay_schedule)
# parqueShopping.set_new_pay_schedule(new_schedule)
# print(parqueShopping.pay_schedule)
# parqueShopping.set_employee_pay_date(11786526)
# print("\nData de pagamento atual do empregado:", emp2.get_payDate())
