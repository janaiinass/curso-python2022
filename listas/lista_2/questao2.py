#Faça um programa que peça um número e verifique se ele é positivo ou negativo 

valor = int(input("Digite um valor positivo ou negativo "))

#Verificando se o valor é maior que zero, logo sendo positivo
if valor > 0: # o comando if para verificar uma expressão e executar um bloco de código caso a condição definida seja verdadeira
    print("O valor", valor, "é positivo")

#Verificando se valor nao for maior que zero, logo ele será negativo
else:
    print("o valor", valor, "é negativo")