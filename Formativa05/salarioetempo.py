salario = float(input("digite seu salário atual: "))
tempserv = float(input("digite seu tempo de serviço em anos: "))
if tempserv > 5:
    salario *= 1.05
    print("você tem direito a bônus! Seu salário será de ",salario)
else:
    print("você não tem direito a bônus, seu salário continuara o mesmo.")