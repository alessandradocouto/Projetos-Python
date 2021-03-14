# Subprogramas

def qtdVogalDig(fr):

    contV = 0
    contD = 0
    contTotalV = 0
    pal = ''
    
    #print(fr) # Alexandre 3

    for p in fr: # 'A' 'l' in 'Alesxandre 3'
        #print(p)
        
        if p in 'aeiou': # 'A' 'l' in 'aeiou'

            contV += 1 # contando cada vogal

        elif p in '0123456789': # '3' in '0123456789'
            
            contD += 1 # contando cada numero

        #print(contV, contD) # 3 1
    
    if contV > contD: # 3 1

        pal = fr

        return pal
   


# Programa Principal

contTotal = 0
contVogal = 0
listaF = []

while True:

    frase = input('Digite: ').strip()
    # 'Alexandre','3'

    if frase == '': # se for vazio sai do loop
        break
    
    else: # caso contrário
        
        # 'Alexandre 3'
        if qtdVogalDig(frase): # se existir, retorna a frase

            contVogal += 1
            listaF.append(qtdVogalDig(frase))

    contTotal += 1


for f in listaF:
    print(f)

print('Total de linhas lidas:', contTotal)
print('Total de linhas com mais vogais que dígitos:', contVogal)