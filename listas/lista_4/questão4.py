#Faça um programa para ler um número inteiro n. Escrever a soma de todos os números pares de 2 até n. Use while.

#Solição de um numero ao usuario e salvando na variavel n
num= int(input("Digite um numero: "))

#Definir o contador igual a 1 para o laço ir de 1 ate o numero escohido 
i = 1
while i <= num:
    if i % 2==0:    #Somar se for par
        soma = i + num
    i +=1 
 
print(f"a soma dos pares é: {soma})")