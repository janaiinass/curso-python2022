#Faça um programa que lê um número inteiro n. Escrever a soma de todos os números de 1 até n. Use while.

#solicitar ao usuario um numero para somar 
num = int(input("Digite um número: "))

#definindo o contador valendo 1 enquanto ele for menor do que o numero que o usuário definido
#somando até o numero escolhido
i = 1
while i <= num:
    soma = num + i
    
    print(f"a soma de {i} + {num} é: {soma}")
    i += 1