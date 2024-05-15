compra = float(input("qual foi o valor da sua compra? "))
if compra > 100:
    compra -= compra * 0.10
    print("você tem direito a desconto, o valor da sua compra será ",compra)
else:
    print("você não tem direito a desconto.")