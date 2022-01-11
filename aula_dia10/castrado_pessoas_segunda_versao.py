# Crie um programa para cadastrar N pessoas.
# Adicione em uma lista e imprima npo final.
n = int(input("Quantas pessoas deseja cadastrar: "))
lista_pessoas = []
for indice in range(n):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    endereço= input (" Digite o endereço: ")
    peso = float(input(" Digite seu peso é:"))
    nova_pessoa = [nome, idade,endereço,peso]
    lista_pessoas.append(nova_pessoa)

for pessoa in lista_pessoas:
    print(f"Olá, {pessoa[0]}, bem-vind@ . Você tem {pessoa[1]} anos! você mora em {pessoa [2]}, seu peso é { pessoa[3]} kg!")

if pessoa[1] <= 18:
    print(" vocé é menor de idade!")
else:
    print(" você é maior de idade!")

print("Quantidade de pessoas cadastradas: ", len(lista_pessoas))