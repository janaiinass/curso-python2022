#faça um programa que peça dois números e imprima o maior deles

num1 = int(input("Digite um número "))
num2 = int(input("Digite outro número "))

#Fazendo a condição para verficicar utlizando' if 'se o 1 num é maior que o 2
if num1 > num2:
    print("o número", num1, "é maior que o", num2)

elif num1 == num2:
    print("os números são iguais")

#Fazendo a condição para verficar utlizando `ELSE` se o 2 num é maior que o 1
else:
    print("o número", num2, "é mai0r que", num1)