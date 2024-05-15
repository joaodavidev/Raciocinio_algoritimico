idade = int(input("digite sua idade: "))
if idade < 12:
    print("você é criança!")
elif idade < 17:
    print("você é adolecente")
elif idade < 59:
    print("você é adulto")
else:
    print("você é idoso")