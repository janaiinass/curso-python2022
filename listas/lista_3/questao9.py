#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

#a quantidade de numeros do conjunto
n = int(input("Digite a quantidade de numeros do conjunto "))
conjunto=[]

# numeros do conjunto e colocando em uma lista
for i in range(n):
    termo = int(input("numero: "))
    conjunto.append(termo)

#Ordenando a lista de forma crescente para pegar o menor e maior valor
conjunto.sort()
print("o menor número é: ", conjunto[0])     # o primeiro e menor item
print("o maior número é: ", conjunto[-1])    #o ultimo e maior numero
print("A soma dos números do conjunto é: ", sum(conjunto)) #a soma ( sum) de todos os itens do conjunto