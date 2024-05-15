def escadinha(n):
    n = int(input('digite um limite: '))
    for i in range(1,n+1):
        lista = []
        for j in range (1,i+1):
            lista.append(j)
        print(lista)
            
escadinha(4)