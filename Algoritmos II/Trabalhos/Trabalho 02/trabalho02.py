#Alunos: Camily Victal Finamor - 2024001197 / Luis Gustavo Riso Santos - 2024002372
#Trabalho 2 da disciplina Algoritmos e Programacao II
#------------------------------------------------------------------------------------------------------------------------------------------
import random

#Funcao de leitura do arquivo csv, onde inserimos as criaturas em um dicionario
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

#------------------------------------------------------------------------------------------------------------------------------------------

#Funcao de leitura dos pesos do usuario, onde ja fazemos o calculo da soma da nota do animal multiplicado pelo peso de acordo com o usuario
def leituraPesos(usuarios, quantidadeUsuarios, criaturas):
    i = 0
    while(i < quantidadeUsuarios):
        usuario = list(map(int, (input("").split())))
        for nomeAnimal, criatura in criaturas.items():
            somaPesos = 0
            for k in range(6):
                somaPesos += usuario[k] * criatura["atributos"][k]
            vetor = [nomeAnimal, somaPesos]
            usuarios[i].append(vetor)
        i += 1

#------------------------------------------------------------------------------------------------------------------------------------------

#Algoritmo de ordenacao para a parte A: Quick-sort
def partition(lista, esq, dir):
    r = random.randint(esq, dir)
    aux = lista[r]
    lista[r] = lista[esq]
    lista[esq] = aux
    j = esq
    pivot = lista[esq] 
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

def quicksort(listaUsuario, esq, dir):
        if esq < dir:
            p = partition(listaUsuario, esq, dir) 
            quicksort(listaUsuario, esq, p-1) 
            quicksort(listaUsuario, p+1, dir) 
    
#------------------------------------------------------------------------------------------------------------------------------------------

#Funcao para unificar a preferencia dos usuarios e calcular a soma dessas preferencias para cada animal
def ranquearAnimais(usuario, criaturas):
    max = 0
    for i in range(len(usuario)):
        usuario[i][1] = i
        #sobrescrevemos a lista de atributos pelo valor da soma final de acordo com as preferencias dos usuarios
        if isinstance(criaturas[usuario[i][0]]["atributos"], list):
            criaturas[usuario[i][0]]["atributos"] = 0
        criaturas[usuario[i][0]]["atributos"] += usuario[i][1]
        if max < criaturas[usuario[i][0]]["atributos"]:
            max = criaturas[usuario[i][0]]["atributos"]
    return max

#------------------------------------------------------------------------------------------------------------------------------------------

#Algoritmo de ordenacao para a parte B: Couting-sort (versao estavel)
def StableCountingSort(lista, maiorPontuacaoCriatura):
    B = [None for _ in range(0, len(lista))]
    C = [0 for _ in range(0, maiorPontuacaoCriatura+1)]

    for a in lista: 
        C[a[1]] += 1 

    for i in range(1, maiorPontuacaoCriatura+1):
        C[i] = C[i] + C[i-1] 
    
    for i in range(len(lista)-1, -1, -1):  
        a = lista[i]
        B[C[a[1]] - 1] = a
        C[a[1]] -= 1 

    #Looping pque faz a verificacao de repeticoes e que ordena alfabeticamente caso a repeticao aconteca
    for i in range(1, len(B)):
        if B[i][1] == B[i - 1][1]:  
            j = i
            while j > 0 and B[j][1] == B[j - 1][1] and B[j][0] > B[j - 1][0]:
                B[j], B[j - 1] = B[j - 1], B[j]
                j -= 1
    
    return B

#------------------------------------------------------------------------------------------------------------------------------------------
#MAIN

#No main fizemos a leitura de entrada com o nome do arquivo e a quantidade de usuarios
#E criamos o dicionario de criaturas e a lista de usuarios
if __name__ == "__main__":
    nomeArquivo = input()
    quantidadeUsuarios = int(input())
    criaturas = {}
    usuarios = [[] for _ in range(quantidadeUsuarios)] 
    leituraArquivo(nomeArquivo, criaturas)
    leituraPesos(usuarios, quantidadeUsuarios, criaturas)

#Ordenamos de acordo com o ranking pessoal dos usuarios e ja fazemos a soma da unificacao de preferencias dos usuarios para os animais
    for i in range(len(usuarios)):
        quicksort(usuarios[i], 0, len(usuarios[i]) - 1)
        maiorPontuacaoCriatura = ranquearAnimais(usuarios[i], criaturas)

#e para o ranking final das criaturas no geral, criamos um vetor auxiliar que sera usado no algoritmo de ordenacao, ja que nossas criaturas estavam
#em um dicionario. Cada slot do nosso vetor contem uma tupla que guarda o nome do animal e a soma da unificacao de preferencias dos usuarios para os animais
    listacriaturas = []
    for nomeAnimal, criatura in criaturas.items():
        dadoCriatura = (nomeAnimal, int(criatura["atributos"]))
        listacriaturas.append(dadoCriatura)
    listacriaturas = StableCountingSort(listacriaturas, maiorPontuacaoCriatura)

#Por fim, imprimimos essas tuplas de animais, exibindo seu nome e sua nota
    for i in range(len(listacriaturas)-1, -1, -1):
        print(f"{listacriaturas[i][0]} {listacriaturas[i][1]}")

