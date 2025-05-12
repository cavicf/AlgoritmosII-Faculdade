def countingSort(lista, valorMaximo):
    vetorContagem = [0 for _ in range(0, valorMaximo+1)]
    listaOrdenada = [None for _ in range(0, len(lista))]
    for valor in lista:
        vetorContagem[valor[1]] += 1
    for i in range(1, valorMaximo+1):
        vetorContagem[i] += vetorContagem[i-1]
    for i in range(len(lista)-1, -1, -1):
        atual = lista[i]
        listaOrdenada[vetorContagem[atual[1]] - 1] = atual
        vetorContagem[atual[1]] -= 1
    return listaOrdenada

lista = [('camily', 2), ('jose', 2), ('pedro', 2), ('rafael', 1)]
lista = countingSort(lista, 2)
print(lista)


def countingSortDecrescente(lista, valorMaximo):
    vetorContagem = [0 for _ in range(0, valorMaximo+1)]
    listaOrdenada = [None for _ in range(0, len(lista))]
    for valor in lista:
        vetorContagem[valor[1]] += 1
    for i in range(valorMaximo-1, -1, -1):
        vetorContagem[i] += vetorContagem[i+1]
    for i in range(len(lista)-1 , -1, -1):
        atual = lista[i]
        listaOrdenada[vetorContagem[atual[1]] - 1] = atual
        vetorContagem[atual[1]] -= 1
    return listaOrdenada

lista = [('camily', 2), ('jose', 2), ('pedro', 2), ('rafael', 1)]
lista = countingSortDecrescente(lista, 2)
print(lista)