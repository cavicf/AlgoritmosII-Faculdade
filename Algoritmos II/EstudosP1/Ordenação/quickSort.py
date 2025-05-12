import random

def quickSort(lista, esquerdo, direito):
    if esquerdo < direito:
        p = partition(lista, esquerdo, direito)
        quickSort(lista, esquerdo, p - 1)
        quickSort(lista, p + 1, direito)

def partition(lista, esquerdo, direito):
    # escolher pivô aleatório e colocar no início
    pivoIndice = random.randint(esquerdo, direito)
    lista[esquerdo], lista[pivoIndice] = lista[pivoIndice], lista[esquerdo]
    pivot = lista[esquerdo]

    i = esquerdo + 1 
    j = direito

    while i <= j:
        while lista[i][1] < pivot[1]:
            i += 1
        while lista[j][1] > pivot[1]:
            j -= 1
        if i <= j:
            lista[i], lista[j] = lista[j], lista[i]
            i += 1
            j -= 1

    # Agora que j está no último elemento menor que o pivot,
    # colocamos o pivot na posição correta
    lista[esquerdo], lista[j] = lista[j], lista[esquerdo]
    print(lista)
    return j

# Exemplo
lista = [('camily', 2), ('jose', 2), ('pedro', 2), ('rafael', 1)]
quickSort(lista, 0, len(lista) - 1)
print(lista)