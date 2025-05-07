def insertionSort(lista):
    for i in range(1, len(lista), 1): #meu for que controla a parte não ordenada, começa em 1 pq assumimos que o primeiro elemento lista[0] sozinho está ordenado
        for j in range(0, i): #meu for que controla a parte ordenada
            if lista[j][1] > lista[i][1]: 
                lista[j], lista[i] = lista[i], lista[j] #faço a troca
                print(lista)


#testando o insertion sort
lista = [('camily', 2), ('jose', 2), ('pedro', 2), ('rafael', 1)]
insertionSort(lista);
print(lista)

