# Faça um Programa que leia N (peça pro usuário informar o valor de N) notas e insira em uma lista, depois percorra a lista e calcule a soma das notas, por fim calcule a média (soma dividido por N) e mostre na tela

#Solicitando ao usuário a quantidade de notas
n = int(input("Digite quantas notas vc quer calular a media: "))

#lista fazia para que no for ela seja preenchida com as notas informadas
lista = []

#  laço para pegar a quantidade de notas informada pelo o user
for x in range (n): #range() retorna um conjunto de números sequenciais
    nota = float(input(f"Digete a nota {x + 1}:"))  #Solicitado a nota ao user  
    lista.append(nota)     #append adiciona um elemento na lista                        


soma = sum(lista) #sum soma os elementos da lista
print("a media é:", soma/n)  