def mergeSort(lista): #parte da divisao 
    if len(lista ) == 1:
        return lista
    meio = len(lista) // 2
    listaEsquerda = mergeSort(lista[:meio])
    listaDireita = mergeSort(lista[meio:])
    return merge(listaEsquerda, listaDireita)

def merge(listaEsquerda, listaDireita): #parte da conquista
    i = 0
    j = 0
    listaOrdenada = []
    while i < len(listaEsquerda) and j < len(listaDireita):
        if listaEsquerda[i][1] <= listaDireita[j][1]:
            listaOrdenada.append(listaEsquerda[i])
            i += 1
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

lista = [('camily', 2), ('jose', 2), ('pedro', 2), ('rafael', 1)]
resultado = mergeSort(lista)
print(resultado)