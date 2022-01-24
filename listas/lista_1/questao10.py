#tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas
#para homens : (72.7*h)-58
#para mulheres (62.1*h)-44.7

#float para trabalharmos com casas decimais e salvar na variavel h
h = float(input("Digite a sua altura: "))

pesoH = (72.7*h)-58 #calculo do peso ideal para homens, salva na variavel pesoH
pesoM = (62.1*h)-44.7 #calculo do peso ideal para homens,  salva na variavel pesoM
print("Se for homem, o peso ideal é:", pesoH)
print("Se for mulher, o peso ideal é:", pesoM) 
