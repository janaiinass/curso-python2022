def soma(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2
    
def div(num1, num2):
    return num1 / num2
       
# Entrada
print("Escolha qual opeção deseja realizar: ")
opcao = input("+, -, /, *:")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == "+":
    valor_soma = soma(num1, num2)
    print(f"{num1} + {num2} == {valor_soma}")   

if opcao == "-":
    valor_soma = soma(num1, num2)
    print(f"{num1} + {num2} == {valor_soma}")   

if opcao == "/":
    valor_soma = soma(num1, num2)
    print(f"{num1} + {num2} == {valor_soma}")  

if opcao == "*":
    valor_soma = soma(num1, num2)
    print(f"{num1} + {num2} == {valor_soma}")    
    
