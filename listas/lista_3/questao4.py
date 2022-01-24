#Faça um Programa que peça o nome, a idade e a altura de N pessoas, armazene cada informação em uma lista e depois insira em uma lista maior chamada lista_pessoas. Por fim, imprima o nome e peso de cada pessoa, e
#diga se ela é maior ou menor de idade.

# quantidade de cadastros
quat = int(input("Digite a quantidade de pessoas que deseja cadastrar: "))

#definindo a lista maior para ser preenchida no for
lista_total = []

#salvar os  dados da quatidade de pessoas definida pelo o use
for x in range(quat):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    h = float(input("Digite a altura: "))