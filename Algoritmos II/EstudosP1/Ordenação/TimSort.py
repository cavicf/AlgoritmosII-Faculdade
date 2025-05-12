def insertionSort(lista):
    for i in range(1, len(lista)):
        j = i - 1
        atual = lista[i]
        while j >= 0 and atual[1] < lista[j][1]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j + 1] = atual
    return lista

def merge(listaEsquerda, listaDireita):
    listaOrdenada = []
    j=0
    i=0
    while i < len(listaEsquerda) and j < len(listaDireita):
        if listaEsquerda[i][1] <= listaDireita[j][1]:
            listaOrdenada.append(listaEsquerda[i])
            i+=1
        else:
            listaOrdenada.append(listaDireita[j])
            j+=1
    while i < len(listaEsquerda):
        listaOrdenada.append(listaEsquerda[i])
        i+=1
    while j < len(listaDireita):
        listaOrdenada.append(listaDireita[j])
        j+=1 
    return listaOrdenada

def timSort(lista, run):
    for i in range(0, len(lista), run):
        lista[i:i+run] = insertionSort(lista[i:i+run])
    runsize = run
    while runsize < len(lista):
        for y in range(0, len(lista), runsize * 2):
            lista[y: y + runsize*2] = merge(lista[y:y+runsize], lista[y+runsize: y + runsize*2])
        runsize *= 2
    return lista

lista = [('camily', 2), ('jose', 2), ('pedro', 2), ('rafael', 1)]
lista = timSort(lista, 2)
print(lista)