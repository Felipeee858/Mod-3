#calcular a idade em anos
import datetime

dia = int(input("Dia de nascimento: "))
mes = int(input("Mês de nascimento: "))
ano = int(input("Ano de nascimento: "))

#data atual
hoje= datetime.date.today()

#objeto com a data de nascimento
data_nascimento=datetime.date(ano,mes,dia)

#calcula a idade
idade=hoje.year - data_nascimento.year
#verificar se ainda não fez anos
if data_nascimento.month > hoje.month or (data_nascimento.month == hoje.mont and data_nascimento.day>hoje.day):
    idade -=1
    
print(idade)