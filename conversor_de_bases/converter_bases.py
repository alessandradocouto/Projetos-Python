# Subprogramas

def reverteEmostra(listaNum): # passa uma lista por parâmetro = [7,0,1]

    if listaNum != []: # se a lista passada por parâmetro for diferente de vazia
        listaNum = listaNum[::-1] # reverto essa lista e coloco nessa variável

    for item in listaNum: # item = 1, item = 0, item = 7
        print(item, end='') # 107
    
    return '' # para ficar 1101 111 31



def conversorBase(num, base):

    lista = []
    while num >= base: # 13 >= 2
        pinteira = num // base # parte inteira = 6
        resto = num % base # resto da divisao = 1
        lista.append(resto) # o valor de resto vai pra lista
        num = pinteira #  a parte inteira fica igual a 6, depois igual a 3...
    if num < base: # se a base for maior que o número, não entra no loop. Exemplo: 1 < 3
        lista.append(num) #  o num = 1 vai para lista

    return lista # retorno essa lista



# Programa Principal

while True:
    
    n = int(input('Digite um número qualquer: '))
    if n < 0:
        break # sai do loop
    else:
        for b in range(2,10):
            baseNum = conversorBase(n,b)
            print(reverteEmostra(baseNum), end=' ')
        print()
    print()
    
