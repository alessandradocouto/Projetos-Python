
def traducaoRnaM(trinca): # 'UUUCUUCAA'

    lista = []
    TraducaoRnaM = []
    lista.append([trinca[:3], trinca[3:6], trinca[6:9]])
    #print(lista) # [ ['UUU', 'CUU', 'CAA'] ]

    rnaAminoacido = {
        'UUU': 'Phe', 
        'CUU': 'Leu',
        'UUA': 'Leu',
        'AAG': 'Lisina',
        'UCU': 'Ser',
        'UAU': 'Tyr',
        'CAA': 'Gln',
    }

    for l in lista:
        #print(l) # ['UUU', 'CUU', 'CAA']
        for rna in l:
            #print(rna) 
            # UUU 
            # CUU 
            # CAA

            for r, aminoacido in rnaAminoacido.items():
                # lendo chave e valor do dict com .items()
                # print(r, aminoacido) 
                # UUU phe 
                # CUU Leu 
                # CAA Gln

                if rna == r: # UUU == UUU
                    TraducaoRnaM.append(aminoacido)
                    # ['Phe', 'Leu', 'Gln']

    return TraducaoRnaM



while True:

    trincaRNA = input('Digite: ').upper().strip()
    esp ='-'

    if trincaRNA == '':
        break

    else:
        if traducaoRnaM(trincaRNA):
            traducaoRNAmsg = traducaoRnaM(trincaRNA)

            for i, valor in enumerate(traducaoRNAmsg):
                print(valor,end=' ')
            print()