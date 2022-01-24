#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule o seu peso ideal, usando a seguinte fórmula
#(72.7*altura)-58 dados do peofessor

# float para trabalhar com casas decimais e salva na variavel h
h = float(input("Digite a sua altura: "))

peso = (72.7*h)-58 #calculo do peso ideal, resultado salva na variavel peso
 
print("Seu peso ideal é:", peso) 