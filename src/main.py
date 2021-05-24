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
print(parqueShopping.employeesList)
f.close()

sindicato = Sindicate(25.31)

while(1):
    hour_value, wage = None, None
    print("Escolha uma opção: ")
    print("0 - Exibir detalhes do empregado\n1 - Adicionar empregado\n2 - Remover empregado\n3 - Lançar um Cartão de Ponto\n4 - Lançar um Resultado Venda\n5 - Lançar uma taxa de serviço\n6 - Alterar detalhes de um empregado\n7 - Rodar a folha de pagamento para hoje\n8 - Agenda de Pagamento\n9 - Criação de Novas Agendas de Pagamento\n\n10 - Sair\n\n")
    op = int(input("Escolha: "))
    if op == 10:
        break
    elif op == 1:
        name = input("Nome: ")
        rg = input("Rg: ")
        adress = input("Endereço: ")
        sindMember = input("Membro do sindicato? Se sim digite 1, se não 0: ")
        print("Tipo de empregado: \n")
        print("1 - Comissionado\n2 - Horista\n3 - Salariado")
        escolha = int(input("Digite a opção: "))
        if escolha == 1:
            emp_type = "Comissioned"
        elif escolha == 2:
            emp_type = "Hourly"
        else:
            emp_type = "Salaried"
        if emp_type == "Hourly":
            hour_value = float(input("Valor da hora de trabalho: "))
        print("Metodo de pagamento: \n")
        print("1 - Crédito em Conta\n2 - Cheque em mãos\n3 - Cheque via correios\n")
        escolha = int(input("Metodo escolhido: "))
        if escolha == 1:
            payMethod = "AccountCredit"
        elif escolha == 2:
            payMethod = "CheckOnHands"
        else:
            payMethod = "DeliveryCheck"
        print("Data do contrato: ")
        date = input("Digite no formato ANO-MES-DIA: ")
        if not hour_value:
            wage = float(input("Salário: "))
        print("Dados bancários: ")
        bankID = input("Banco: ")
        agency = input("Agência: ")
        account = input("Conta: ")
        parqueShopping.add_employee(emp_type=emp_type, sindMember=sindMember, date=date, name=name, rg=rg, adress=adress, bankAcc={'bankID':bankID, 'agency':agency, 'account':account}, payMethod=payMethod, wage=wage)
        print(parqueShopping.employeesList)
    elif op == 2:
        id = int(input("Digite o ID do empregado que deseja remover: "))
        parqueShopping.remove_employee(id)
        print(parqueShopping.employeesList)
    elif op==3:
        id = int(input("ID do empregado: "))
        date = input("Data do ponto: ")
        hours = float(input("Horas trabalhadas: "))
        parqueShopping.timeRegister(id, date, hours)
    elif op==4:
        id = int(input("ID do empregado: "))
        date = input("Data da venda: ")
        value = float(input("Valor da venda: "))
        parqueShopping.set_sale_to_employee(id, date, value)
    elif op==5:
        id = int(input("ID do empregado: "))
        tax_value = float(input("Valor da taxa: "))
        sindicato.tax_associator(id, tax_value)
    elif op==6:
        id = int(input("ID do empregado: "))
        print("Escolha o atributo que deseja alterar: ")
        while(1):
            print("1 - Tipo de empregado\n2 - Nome\n3 - RG\n4 - Endereço\n5 - Dados Bancários\n6 - Método de pagamento\n7 - Salário\n8 - Valor da hora de trabalho\n\n9 - Alterar\n10 - Sair sem alterar")
            emp_type, name, rg, bankID, agency, account, payMethod, new_wage, hour_value = None, None, None, None, None, None, None, None, None
            opcao = int(input())
            if opcao == 1:
                print("Tipo de empregado: \n")
                print("1 - Comissionado\n2 - Horista\n3 - Salariado")
                escolha = int(input("Digite a opção: "))
                if escolha == 1:
                    emp_type = "Comissioned"
                elif escolha == 2:
                    emp_type = "Hourly"
                else:
                    emp_type = "Salaried"
                if emp_type == "Comissioned":
                    hour_value = float(input("Valor da hora de trabalho: "))
            elif opcao == 2:
                name = input("Nome: ")
            elif opcao == 3:
                rg = input("RG: ")
            elif opcao == 4:
                adress = input("Endereço: ")
            elif opcao == 5:
                bankID = input("Banco: ")
                agency = input("Agência: ")
                account = input("Conta: ")
            elif opcao == 6:
                print("1 - Crédito em Conta\n2 - Cheque em mãos\n3 - Cheque via correios\n")
                escolha = int(input("Novo método: "))
                if escolha == 1:
                    payMethod = "AccountCredit"
                elif escolha == 2:
                    payMethod = "CheckOnHands"
                else:
                    payMethod = "DeliveryCheck"
            elif opcao == 7:
                new_wage = float(input("Salário: "))
            elif opcao == 8:
                hour_value = float(input("Valor da hora de trabalho: "))
            elif opcao == 9:
                parqueShopping.change_employee_details(id, emp_t=emp_type, name=name, rg=rg, adress=adress, bankAcc={'bankID':bankID, 'agency':agency, 'account':account}, payMethod=payMethod, wage=new_wage)
                print("Dados alterados!\n\n")
                break
            elif opcao == 10:
                break
    elif op == 7:
        date = input("Data para rodar a folha de pagamento (AAAA-MM-DD): ")
        parqueShopping.pay_employees(date)
    elif op == 8:
        id = int(input("ID do empregado: "))
        parqueShopping.set_employee_pay_date(id)
        print("Data alterada!")
    elif op == 9:
        print("Quantas datas deseja criar? ")
        i = int(input())
        for c in range(i):
            schedule = []
            t = input("1 - weekly-1\n2 - weekly-2\n3 - Monthly\n0 - Sair")
            if t == 0:
                break
            else:
                if t == 1:
                    prazo = "weekly-1"
                elif t == 2:
                    prazo = "weekly-2"
                else: prazo = "monthly"
                if prazo == "monthly":
                    print("\nSe o dia for o último dia útil do mês escreva 'util'\n")
                    t = input("Dia: ")
                    if t == "util":
                        dia = "$"
                    else:
                        dia = t
                else:
                    t = input("Dia: ")
                final = prazo+"-"+dia
                escolha = input("Adicionar data a agenda? 1 - SIM / 2 - NAO: ")
                if escolha == 1:
                    schedule.append(final)
        if len(schedule) >= 1:
            parqueShopping.set_new_pay_schedule(schedule)
            print(parqueShopping.pay_schedule)
            print("\n")
    elif op == 0:
        id = int(input("ID do Empregado: "))
        i = parqueShopping.get_employee(id)
        emp = parqueShopping.employeesList[i]
        wage, hour_value = 0, 0
        if isinstance(emp, Hourly):
            emp_t = "Horista"
            hour_value = emp.hour_value
        elif isinstance(emp, Salaried):
            emp_t = "Assalariado"
            wage = emp.wage
        else:
            emp_t = "Comissionado"
            wage = emp.wage
        print("\n\nID:",emp.id,"\nTipo de Empregado:",emp_t, "\nNome:", emp.name,"\nRG:", emp.rg,"\nEndereco", emp.adress,"\nMembro do Sindicato:", emp.sindMember,"\nDados Bancarios:", emp.bankAcc,"\nMetodo de pagemento:", emp.paymentMethod, "\nData de pagemento:", emp.payDate, "\nSalario:", wage, "\nValor da hora de trabalho:", hour_value, "\n\n")
    elif op == 11:
        break

            
            

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
