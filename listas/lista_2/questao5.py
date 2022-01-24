#Faça um programa que verifique se a letra digitada é uma vogal ou consoante

#Solicitando ao user uma letra
letra = input("Digite una letra ")

#Verificando se a letra digitada é uma vogal ou consoante
if letra in ("a","e","i","o","u"):
    print(letra, "é uma vogal")

else:
    print(letra,"é uma consoante") 

    #fazer tratamento de erro antes do else, colocar um elif obs: pois quando coloca numero ou caracteres mostra que é consoante