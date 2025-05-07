def insertionSort(lista):
    for i in range(1, len(lista), 1): #meu for que controla a parte não ordenada, começa em 1 pq assumimos que o primeiro elemento lista[0] sozinho está ordenado
        valorInserir = lista[i]
        indiceAnterior = i
        while indiceAnterior > 0 and lista[indiceAnterior-1][1] > valorInserir[1]: #meu looping que controla a parte ordenada
            lista[indiceAnterior] = lista[indiceAnterior - 1]
            indiceAnterior -= 1
        lista[indiceAnterior] = valorInserir

#testando o insertion sort
lista = [('camily', 2), ('jose', 2), ('pedro', 2), ('rafael', 1)]
insertionSort(lista);
print(lista)

