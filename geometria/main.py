import area

opcao= int(input("escolha uma opção: 1. circulo, 2. quadrado: "))

if opcao == 1:
    circ= float(input("Qual o valor do raio? "))
    print("a area do circulo é:", area.circulo(circ))

elif opcao == 2:
    quad= float(input("Digite o valor do lado do quadrado: "))
    area_quad = area.quadrado(quad)
    print("a area do quadrado é:", area_quad)

else:
    print("escolha invalida")
