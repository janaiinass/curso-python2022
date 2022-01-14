#programa para saber o dia da semana do nascimento
import datetime


ano=int(input("digite o ano do seu nascimento:  "))
mes=int(input(" digite o mês do seu nascimento: "))
dia=int(input( "digite o dia do seu nascimento: "))

data_n=datetime.datetime(ano,mes,dia)

print(data_n.strftime(" o dia da semana que você nasceu foi : %A"))