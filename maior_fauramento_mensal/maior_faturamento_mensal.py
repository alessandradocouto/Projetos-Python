# Subprogramas

def totalFaturamento(fat):

    somaF = 0

    for i in fat.values():
    
        somaF += float(i)

    return somaF #  faturamento total



def faturamentoM(fa, s):

    fatuE = {}
    for key, value in fa.items():

        value = (value * 100) / s
        fatuE[key] = value

    return fatuE



def mostra(di):

    for k, v in di.items():
        print('O faturamento mensal de {} em relação ao total: {:.3f}%'.format(k,v))



#Programa Principal

faturamento = {'São Paulo': 67.83643, 'Rio de Janeiro': 36.67866, 'Minas Gerais': 29.22988, 'Espirito Santo': 27.16548, 'outros': 19.84953}

totalF = totalFaturamento(faturamento)
totalFatMensal = faturamentoM(faturamento, totalF)
print('O faturamento mensal total foi de {:.3f}'.format(totalF))
mostra(totalFatMensal)
