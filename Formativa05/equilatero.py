lado1 = float(input("digite o lado 1: "))
lado2 = float(input("digite o lado 2: "))
lado3 = float(input("digite o lado 3: "))
if lado1 == lado2 == lado3:
    print("tirangulo equilatero!")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("triangulo isóceles!")
else:
    print("triangulo escaleno!")