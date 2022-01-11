# programa que o usuario e a senha não aceite ser igual
while True:
    usuario = input("Digite o nome do usuario: ")
    senha = input(" digite uma senha: ")
    if (usuario != senha):
        print(" usuario castrado, senha valida!  ")
        break
    else:
         print( "usuario não castrado, senha invalida! tente novamente. ")
    