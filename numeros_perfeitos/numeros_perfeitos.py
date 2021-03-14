# Subprograma

def numeroPerfeito(n):

    somaP = 0
    listaNP = []

    for i in range(1, n):

        if n % (n-i) == 0:

            listaNP.append(n-i) # [3,2,1]

    for num in listaNP:

        somaP += num # 3+2+1 = 6

    if somaP == n:
        return n



 
# Programa Principal

cont = 0

while True:

    numeros = list(map(int,input('Digite: ').split()))

    ''' entrada do usuário com listas de inteiros em 1 linha '''
    
    cont += 1
    
    if numeros == [] and cont == 1:

        print('Nenhum Número Foi Lido!!!')
        break

    if numeros == []:
        break

    break

        
for item in numeros: 
    ''' passando cada item da lista pra função '''  
    # [999, 496, 13, 8, 28, 2, 1, 6, -29, 37, 8128, 6, 1024]
    if numeroPerfeito(item):
        # numeroPerfeito(6)
        print(item,'é um número perfeito')

