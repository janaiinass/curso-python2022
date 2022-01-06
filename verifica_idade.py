#vericação de idade
idade=int(input("digite a data de nascimento: "))
calcule=2022-idade

if calcule >=18:
  print('você é maior de idade, sua idade é:', calcule)

if calcule < 18:
    print('você é menor de idade, sua idade é: ', calcule)
