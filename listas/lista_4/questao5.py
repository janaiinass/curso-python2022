# Faça um programa que lê um número inteiro n. E verifique se n é um número par, se não for pedir para inserir outro número até que seja par. Use while.


while True:

    n = int(input("Digite um número: "))  #para While com true, usar o print dentro do laço

    if n % 2 != 0:                        #Se o numero digitado seja impar o programa continua executando (True)
        print("O número é impar, digite um número par! ")

    else:  
        print("O número é par!")                               #se o número for par entra o break e o programa para a execução
        break