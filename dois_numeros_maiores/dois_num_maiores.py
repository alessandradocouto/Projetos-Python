
# Subprograma

def doisMaioresNumeros(lista):
    #exemplos:
    # [2,4,7,-5]
    # [3,-9]
    maior1 = lista[0] # 7 ou # 3
    maior2 = 0 # 4

    for j in range(0, len(lista)):
        if lista[j] > maior1: # 7 > 4
            maior1, maior2 = lista[j], maior1 #segundo maior:6
            # maior1 = 7
            # maior2 = 4
        elif maior1 > lista[j] and lista[j] > maior2:
            # maior1 > item > maior2
            # 3 > -9 and -9 > 0
            maior2 = lista[j]
            # maior2 = item
            # maior2 =  


    if maior2:
        return maior1, maior2 # retorna os dois maiores
    else:
        return maior1 # retorna 1 só numero, pois há um maior



#Programa Principal

listaNum = []  # lista vazia
while True:

    n = int(input('Numeros: '))
    listaNum.append(n) # add na lista

    if n < 0: # se numero for negativo sai do loop
        break

if len(listaNum) == 1: # tamanho da lista igual a 1, num é negativo
    print('Nenhum valor válido!!!')

elif len(listaNum) == 2: # Há um só numero positivo
    print('Apenas um valor foi lido:', doisMaioresNumeros(listaNum))

else:
    if len(listaNum) > 2:
        print('Os dois maiores números lidos foram: ', end='')
        for i in doisMaioresNumeros(listaNum):
            print(i, end=' ')
    print()

