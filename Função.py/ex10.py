def fibonacci(n):
    lista = []
    soma = 1
    j = 1
    for i in range (n):
        lista.append(soma)
        soma += j
        j = soma - j
    print(lista)
fibonacci(8)


