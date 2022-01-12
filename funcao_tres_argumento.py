#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
def soma (num1, num2 , num3):
    soma= num1 + num2 + num3
    return soma 

num1 =float(input("digite o primeiro numero: "))
num2 =float(input("digite o segundo numero: "))
num3 =float(input("digite o terceiro numero: "))
result= soma (num1, num2, num3)
print(result)