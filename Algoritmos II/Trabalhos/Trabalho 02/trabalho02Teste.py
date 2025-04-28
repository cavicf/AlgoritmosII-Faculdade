import random

#Leitura dos animais + pontuação dos seus atributos

def leituraArquivo(brainrot, criaturas):
    with open(brainrot, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        
        for linha in linhas[1:]:
            criaturaAtual = linha.strip().split(',')
            nome = criaturaAtual[0]
            atributos = list(map(float, criaturaAtual[1:]))

            criatura = {
                "nome": nome,
                "atributos": atributos
            }
            criaturas.append(criatura)

#----------------------------------------------------------------------------------------------------------------------

#Funcao de leitura do pesos + soma das notas por animal

def leituraPesos(usuarios, quantidadeUsuarios, criaturas):
    i = 0
    while(i < quantidadeUsuarios):
        usuario = list(map(int, (input("").split())))
        #usuarios.append(usuario) #vetor com 5 pesos []
        for j in range(0, len(criaturas), 1):
            somaPesos = 0
            for k in range(6):
                somaPesos += usuario[k] * criaturas[j]["atributos"][k]
            vetor = [criaturas[j]["nome"], somaPesos]
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
    for i in range(len(usuario)):
        usuario[i][1] = i
        for j in range(len(criaturas)):
            if usuario[i][0] == criaturas[j]["nome"]:
                if isinstance(criaturas[j]["atributos"], list):
                    criaturas[j]["atributos"] = 0
                criaturas[j]["atributos"] += usuario[i][1]
                
#----------------------------------------------------------------------------------------------------------------------

#Funcao para ranquear animais

def StableCountingSort(lista, k):
    B = [None for _ in range(0, len(lista))]
    C = [0 for _ in range(0, k+1)]

    for a in lista: 
        C[a["atributos"]] += 1 

    for i in range(1, k+1):
        C[i] = C[i] + C[i-1]

    for i in range(len(lista)-1, -1, -1):  
        a = lista[i]
        B[C[a["atributos"]] - 1] = a
        C[a["atributos"]] -= 1 
    
    return B

#----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    nomeArquivo = input()
    quantidadeUsuarios = int(input())
    criaturas = []
    usuarios = [[] for _ in range(quantidadeUsuarios)] 
    leituraArquivo(nomeArquivo, criaturas)
    #print(criaturas)
    leituraPesos(usuarios, quantidadeUsuarios, criaturas)
    #for i in range(len(usuarios)):
    #    print(usuarios[i])
    #print("\n\n")
    for i in range(len(usuarios)):
        quicksort(usuarios[i], 0, len(usuarios[i]) - 1)
    #for i in range(len(usuarios)):
    #    print(usuarios[i])
    #print("\n\n")
        ranquearAnimais(usuarios[i], criaturas)
    #for i in range(len(usuarios)):
    #    print(usuarios[i])
    #print("\n\n")
    k = max(c['atributos'] for c in criaturas)
    criaturas = StableCountingSort(criaturas, k)
    for i in range(len(criaturas)-1, -1, -1):
        print(f"{criaturas[i]['nome']}: {criaturas[i]['atributos']}")

