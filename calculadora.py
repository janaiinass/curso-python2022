#calculadora
def soma(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2
    
def div(num1, num2):
    return num1 / num2

# Entrada
print("Escolha a operação ")
operacao = input("+, -, /, *:  ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if operacao == "+":
    valor_soma = soma(num1, num2)
    print(f"{num1} + {num2} == {valor_soma}")   

if operacao == "-":
    valor_sub = sub(num1, num2)
    print(f"{num1} - {num2} == {valor_sub}")   

if operacao == "*":
    valor_mult = mult(num1, num2)
    print(f"{num1} * {num2} == {valor_mult}")  

if operacao == "/":
    valor_div = div(num1, num2)
    print(f"{num1} / {num2} == {valor_div}")    
    
print("operação valida")
