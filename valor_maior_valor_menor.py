#Faça um programa que, dado um conjunto de Números, determine o menor valor, o maior valor e a soma dos valores.
conj = []
i=0

quantidade = int(input("Digite a quantiade de número que deseja digitar: "))
while quantidade != i:
    numero = conj.append(float(input("Digite um número: "))) #usei o appende para  registrar um numero apos o ultimo elemento
    i += 1

print("conjunto de números: ", conj, "\nNúmero Maior: ", max(conj), "\nNúmero Menor: ", min(conj)) #\n pular linha
print("Soma: ", max(conj) + min(conj)) #max e min, para achar o maior e menor valor.