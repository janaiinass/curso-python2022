#faça um programa que pergunte quanto vc ganha por hora e o numero de horas trabalhadas no mês. Calcule e mostre o total do seu salario no referido mês

valor = float(input("Qual o valor da sua hora de trabalho? ")) 
horas = float(input("Quantas horas voce trabalhou nesse mês? ")) 

salario = valor*horas # o resultado salario salvo  na vairavel salario

print("Seu salario deste mês é de R$: ",salario)