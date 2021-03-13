# Subprogramas

def qtdVogal(palavra):

    for p in palavra:

        if p in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            
            return True

    return False




def palind(lista):
    
    listaP = []
    cont = 0
    contP = 0

    for i, valor in enumerate(lista):

        if valor[::-1] == valor: # palavra reversa
            # vou chamar de palind
            palind = valor[::-1]
            # acrescento ela numa listaP
            listaP.append(palind)

            # é palind e tem vogal?
            contP += 1  # incremento a quantidade de palavras palindromes

        cont += 1 # incremento a qtd total palavras palindromes
        

    return cont, contP, listaP 



# Programa Principal

listaPalavra = []
contPalV = 0
while True:
    
    pal = input('Digite uma palavra: ').lower().strip()

    if pal == '':
        break

    else:
        listaPalavra.append(pal)
    
    if palind(listaPalavra): # se funcao existe
        
        totalPal, totalPalind, listaPal = palind(listaPalavra)

        if pal in listaPal: # se cada palavra tá dentro da lista da funcao
            print('É palíndrome!')
            
            if qtdVogal(pal):
                contPalV += 1
        else:
            print('Não é palíndrome!')

        
print('Quantidade de palavras:', totalPal)
print('Quantidade de palavras palindromes:', totalPalind)
print('Quantidade de palavras palindromes que tem vogais:', contPalV)

