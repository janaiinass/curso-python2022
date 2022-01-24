#Faça um programa que leia números reais. Quando o número digitado for o número zero o programa deverá apresentar uma lista com todos os números que foram digitados e sair do laço while.Use while.

#lista para guardar os numeros
lista = []


while True: #while faz com que um conjunto de instruções seja executado enquanto uma condição é atendida. 
    num = float(input("Digite o numero: "))
    
    
    #o numero digitado seja diferente de zero ele salva o numero na lista
    if num != 0:
        lista.append(num)

    #quando o numero for o 0, mostrar a lista com todos o números digitados      
    else:
        print(lista)
        break#Ao encontrar a declaração break, o programa interrompe a execução do bloco de código e o controle passa para a primeira linha após o laço.
        