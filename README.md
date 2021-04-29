# Disciplina: Projeto de Software
## Professor: Baldoino Fonseca dos Santos Neto

#### Sistema de Folha de Pagamento

O objetivo do projeto é construir um sistema de folha de pagamento. O sistema consiste do
gerenciamento de pagamentos dos empregados de uma empresa. Além disso, o sistema deve
gerenciar os dados destes empregados, a exemplo os cartões de pontos. Empregados devem receber
o salário no momento correto, usando o método que eles preferem, obedecendo várias taxas e impostos deduzidos do salário.

• Alguns empregados são horistas. Eles recebem um salário por hora trabalhada. Eles
submetem "cartões de ponto" todo dia para informar o número de horas trabalhadas naquele dia. Se um empregado trabalhar mais do que 8 horas, deve receber 1.5 a taxa normal Durante as horas extras. Eles são pagos toda sexta-feira.

• Alguns empregados recebem um salário fixo mensal. São pagos no último dia útil do mês(desconsidere feriados). Tais empregados são chamados "assalariados".

• Alguns empregados assalariados são comissionados e portanto recebem uma comissão, um
percentual das vendas que realizam. Eles submetem resultados de vendas que informam a data e valor da venda. O percentual de comissão varia de empregado para empregado. Eles são pagos a cada 2 sextas-feiras; neste momento, devem receber o equivalente de 2 semanas de salário fixo mais as comissões do período.

👉 Empregados podem escolher o método de pagamento.

👉 Podem receber um cheque pelos correios

👉Podem receber um cheque em mãos

👉Podem pedir depósito em conta bancária

####Code Smells

• Alguns empregados pertencem ao sindicato (para simplificar, só há um possível sindicato).
O sindicato cobra uma taxa mensal do empregado e essa taxa pode variar entre
empregados. A taxa sindical é deduzida do salário. Além do mais, o sindicato pode
ocasionalmente cobrar taxas de serviços adicionais a um empregado. Tais taxas de serviço
são submetidas pelo sindicato mensalmente e devem ser deduzidas do próximo
contracheque do empregado. A identificação do empregado no sindicato não é a mesma da
identificação no sistema de folha de pagamento.

• A folha de pagamento é rodada todo dia e deve pagar os empregados cujos salários vencem naquele dia. O sistema receberá a data até a qual o pagamento deve ser feito e calculará o pagamento para cada empregado desde a última vez em que este foi pago.



1. Long Method: 
	1.1 The size of the parameter list
	1.2 You are getting several values from an object and
	passing these values as parameters in a method call
	1.3 You have a group of parameters that
	naturally go together - Data Clumps
	1.4 A method is trying to do too much
	1.5 The amount of switch statement for dispatching
	and handling request
	1.6 The amount of switch statement to gather data from
	numerous classes with different interfaces
	1.7 The amount of switch statement to gather data from
	numerous classes with different interfaces
	
2. Large Class:
	Fields and methods

3. Shotgun Surgery:
	When every time you make a kind of change, you have to make a lot of
	Little changes to a lot of different classes

4. Feature Envy:
	A method that seems more interested in a class
	other than the one it actually is in.

5. Lazy Class:
	A class that is not doing enough to pay for itself.

6. Message Chains:
	Example: object.getE().getD().getC().getB().getA().getValue();

*7. Indecent Exposure: "This really happen?"
	Methods or classes that ought not to be visible to clients are
	publicly visible to them
  
  
