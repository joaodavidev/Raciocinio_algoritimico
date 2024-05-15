def somaimposto(taxaimposto,custo):
    n = int(input('quantos itens foram comprados? '))
    #Preço sem imposto total
    preçototal = custo * n
    #Imposto sobre cada item
    imposto = (taxaimposto/100) * custo
    #Imposto total dos itens
    impostototal = imposto * n
    #Custo total com imposto
    custototal = preçototal + impostototal
    
    print(f'o preço sem impostos é {preçototal}')
    print(f'o imposto sobre cada item é {imposto}')
    print(f'o imposto total é {impostototal}')
    print(f'o custo total das coisas é {custototal}')

somaimposto(50,30)