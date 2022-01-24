#Faça um programa que peça 2 numeros inteiros  um real. Calcule e mostre
# 1 - o produto do dobro do primeiro com metado do segundo , 2 - soma do triplo do primeiro com o terceiro, 3 - terceiro elevado ao cubo


num1 = int(input("Digite o primeiro número inteiro ")) 
num2 = int(input("Digite o segundo número inteiro ")) 
num3 = float(input("Digite o terceiro número real ")) #Solcitando o 3 numero do tipo float para trabalhar as casas decimais, pois é numero real

a = (num1*2)*(num2/2) # 1 operaçao salva na variavel a
b = (num1*3)+ num3    # 2 operação salva na variavel b
c = num3**3           # 3 operação salva na variavel c, ** é o operador para potencia no Py

print("o produto do dobro do primeiro com metado do segundo. é: ", a) 
print("soma do triplo do primeiro com o terceiro, é: ", b) 
print("terceiro elevado ao cubo, é: ", c)  
