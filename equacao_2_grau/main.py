import equacao2

A=float(input(" digite o valor A: "))
B=float(input(" digite o valor B: "))
C=float(input(" digite o valor C: "))
d= equacao2.delta(A,B, C)


if d >= 0:
    print (f' a equação definida é : { A}X**2 + {B} -{C}')
    
    X1= equacao2.delta1(A,B,d)
    X2= equacao2.delta2(A,B,d)

    print(f' os valores das raizes da equação são {X1} , {X2}')

else:
    print(" não existem raizes ")