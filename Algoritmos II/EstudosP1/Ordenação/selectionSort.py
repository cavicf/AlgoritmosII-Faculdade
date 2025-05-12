def selectionSort(lista):
    for i in range(len(lista)):
        menorIndice = i
        for j in range(1, len(lista)):
            if lista[j][1] < lista[menorIndice][1]:
                menorIndice = j
        lista[i], lista[menorIndice] = lista[menorIndice], lista[i]

def selectionSortEstavel(lista):
    for i in range(len(lista)):
        menorindice = i
        for j in range(i+1, len(lista)):
            if lista[j][1] < lista[menorindice][1]:
                menorindice = j
        menor = lista[menorindice]
        while menorindice > i:
            lista[menorindice] = lista[menorindice - 1]
            menorindice -= 1
        lista[i] = menor
        
lista = [('camily', 2), ('jose', 2), ('pedro', 2), ('rafael', 1)]
selectionSortEstavel(lista);
print(lista)