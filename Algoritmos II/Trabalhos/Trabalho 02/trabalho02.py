import random

#Leitura dos animais + pontuação dos seus atributos

def leituraArquivo(brainrot, criaturas):
    with open(brainrot, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        
        for linha in linhas[1:]:
            criaturaAtual = linha.strip().split(',')
            nome = criaturaAtual[0]
            atributos = list(map(float, criaturaAtual[1:]))

            criaturas[nome] = {
                "atributos": atributos
            }

#----------------------------------------------------------------------------------------------------------------------

#Funcao de leitura do pesos + soma das notas por animal

def leituraPesos(usuarios, quantidadeUsuarios, criaturas):
    i = 0
    while(i < quantidadeUsuarios):
        usuario = list(map(int, (input("").split())))
        #usuarios.append(usuario) #vetor com 5 pesos []
        for nomeAnimal, criatura in criaturas.items():
            somaPesos = 0
            for k in range(6):
                somaPesos += usuario[k] * criatura["atributos"][k]
            vetor = [nomeAnimal, somaPesos]
            usuarios[i].append(vetor)
        i += 1

#----------------------------------------------------------------------------------------------------------------------

#Algoritmo de ordenação para a parte A

def partition(lista, esq, dir):
    r = random.randint(esq, dir)
    aux = lista[r]
    lista[r] = lista[esq]
    lista[esq] = aux
    j = esq
    pivot = lista[esq] #vetor[nome, nota, -1]
    for k in range(esq+1, dir+1, 1):
        if lista[k][1] < pivot[1]: 
            j += 1
            aux = lista[k]
            lista[k] = lista[j]
            lista[j] = aux
        elif lista[k][1] == pivot[1] and lista[k][0] > pivot[0]:
            j += 1
            aux = lista[k]
            lista[k] = lista[j]
            lista[j] = aux
    lista[esq] = lista[j]
    lista[j] = pivot
    return j

def quicksort(listaUsuario, esq, dir): #recebe os indices de onde comeca a lista e onde termina a lista | indices inclusive
    if esq < dir:
        p = partition(listaUsuario, esq, dir) #descobre a posicao que o p (pivot) estah
        quicksort(listaUsuario, esq, p-1) #puxa a lista da esquerda e o proprio pivot ja estah certo
        quicksort(listaUsuario, p+1, dir) #puxa a lista da direita
    
#----------------------------------------------------------------------------------------------------------------------

#Funcao para ranquear animais

def ranquearAnimais(usuario, criaturas):
    max = 0
    for i in range(len(usuario)):
        usuario[i][1] = i
        if isinstance(criaturas[usuario[i][0]]["atributos"], list):
            criaturas[usuario[i][0]]["atributos"] = 0
        criaturas[usuario[i][0]]["atributos"] += usuario[i][1]
        if max < criaturas[usuario[i][0]]["atributos"]:
            max = criaturas[usuario[i][0]]["atributos"]
    return max

#----------------------------------------------------------------------------------------------------------------------

#Funcao para ranquear animais

def StableCountingSort(lista, maiorPontuacaoCriatura):
    B = [None for _ in range(0, len(lista))]
    C = [0 for _ in range(0, maiorPontuacaoCriatura+1)]

    for a in lista: #o 'a' eh o proprio valor que estah contido no vetor
        C[a[1]] += 1 #vai contabilizar 1 sempre que o valor aparecer

    for i in range(1, maiorPontuacaoCriatura+1):
        C[i] = C[i] + C[i-1] #transforma o vetor C de uma lista de frequência
    
    for i in range(len(lista)-1, -1, -1):  
        a = lista[i]
        B[C[a[1]] - 1] = a
        C[a[1]] -= 1 

    #Adicionado um looping para alterar a ordem alfabetica apos ordenacao previa do CountingSort
    for i in range(1, len(B)):
        if B[i][1] == B[i - 1][1]: #verifica se os valores forem iguais
            j = i
            while j > 0 and B[j][1] == B[j - 1][1] and B[j][0] > B[j - 1][0]: #looping para alterar todos os valores iguais continuamente
                B[j], B[j - 1] = B[j - 1], B[j]
                j -= 1
    
    return B

#----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    nomeArquivo = input()
    quantidadeUsuarios = int(input())
    criaturas = {}
    usuarios = [[] for _ in range(quantidadeUsuarios)] 

    leituraArquivo(nomeArquivo, criaturas)
    leituraPesos(usuarios, quantidadeUsuarios, criaturas)

    for i in range(len(usuarios)):
        quicksort(usuarios[i], 0, len(usuarios[i]) - 1)
        maiorPontuacaoCriatura = ranquearAnimais(usuarios[i], criaturas)

    #------------------------------------------------------------------------------
    #for i in range(len(usuarios)):
    #     print(usuarios[i])
    #print("\n")
    #for nomeAnimal, criatura in criaturas.items():
    #     print(f"{nomeAnimal}: {criatura["atributos"]}")
    #print("\n")
    #------------------------------------------------------------------------------
    #print(maiorPontuacaoCriatura)
    listacriaturas = []
    for nomeAnimal, criatura in criaturas.items():
        dadoCriatura = (nomeAnimal, int(criatura["atributos"]))
        listacriaturas.append(dadoCriatura)
    #print(listacriaturas)
    listacriaturas = StableCountingSort(listacriaturas, maiorPontuacaoCriatura)

    for i in range(len(listacriaturas)-1, -1, -1):
        print(f"{listacriaturas[i][0]} {listacriaturas[i][1]}")

