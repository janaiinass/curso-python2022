def soma(a,b,c):
    res = a + b + c
    return res
def menu():
    a = int(input('Primeiro numero: '))
    b = int(input('Segundo numero : '))
    c = int(input('Terceiro numero: '))

    print('Soma: ', soma(a,b,c))