myHash = {"Maria":2.7, "Carlinhos":10, "Joao":9, "Alessandro":0.1}
aprovados ={}
reprovados ={}
for i in myHash:
    if (myHash.get(i) >= 7):
        aprovados[i] = myHash.get(i)
    else:
        reprovados[i] = myHash.get(i)

print(myHash)
print(aprovados)
print(reprovados)