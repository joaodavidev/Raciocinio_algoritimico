dragonball = {'Goku':['Super sayajin','Super sayajin deus','super sayajin blue'],'Vegeta':['Super sayajin m','Super sayajin 3']}
dragonball['Goku'] = input('digite uma transformação: ')

print(dragonball)
dragonball.pop(input('digite oq remover: '))
print(dragonball)
z = input('qual a chave quer verificar? ')
x = input("verificação: ") in dragonball[z]
print(x)