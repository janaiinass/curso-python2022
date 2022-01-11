#Faça um programa que, dado um conjunto de Números, determine o menor valor, o maior valor e a soma dos valores.
soma=0
numero=[]

while condition:
    num=int(input('Digite o numero: '))

    if num != 0:
        soma += num
        numero.append(num)
    else:
        break

print('Soma: ', soma)
print('Menor Valor: ', min(numero))
print('Maior Valor: ', max(numero))