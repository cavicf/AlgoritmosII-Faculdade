#O principio da Divisão e Conquista é um paradigma de projeto de algoritmos
# É dividido em 3 fases:
# 1- divisão O(1)
# 2- conquista  
# 3- combinação
#Basicamente divide problemas grandes em problmeas menores mais fáceis de resolver, como numa recursão.
#O algoritmo que geralmente é associado a esse paradigma é o merge-sort
#Depois de ordenar as partes pequenas (conquista), temos que juntar essas duas listas em uma só, resultando em uma lista maior de elementos ordenados.
#Vamos copiar para uma nova lista maior, sempre comparando os menores elementos das sublistas ordenadas, ou seja a posição 0 e vou caminhando nelas conforme as comparações vão acontecendo
#Essa nova lista ordenada se chama merge ou intercalação

#MERGE-SORT - O(nLogn) é melhor para ordenar listas muito grandes, mas usa o dobro da memória pois precisa de memória auxiliar nas cópias que vai fazendo 
#Mas é muito melhor que O(n²)

import sys
import random

def merge(listaA, listaB): #Recebe as duas sublistas ordenadas e faz a junção delas. Essa função de merge tem um grau de complexidade de O(n)
    lista = [] #cria uma lista vazia que vai receber a junção das duas sublistas
    i = 0  #inicia uma variavel pra percorrer a lista A
    j = 0 #inicia uma variável pra percorrer a lista B
    while i < len(listaA) and j < len(listaB): #Inicia o looping que percorre as duas juntas, mas em algum momento uma lista vai acabar antes que a outra
        if listaA[i] < listaB[j]: #compara se o elemento da lista A é menor que o da lista B
            lista.append(listaA[i]) #Se for, appendamos o elemento da lista A na lista que recebe o merge
            i+=1 #incremento para o próximo item da lista A, pois ja foi colocado em seu devido lugar na lista que recebe o merge, por isso nesse momento a lista A é menor que a lista B e pode acabar o seu loop primeiro 
        else:
            lista.append(listaB[j]) #Se não, quer dizer que o elemento da lista B é o menor, então appendamos ele 
            j+=1#incremento para o próximo item da lista B, pois ja foi colocado em seu devido lugar na lista que recebe o merge, por isso nesse momento a lista B é menor que a lista A e pode acabar o seu loop primeiro 
    #Ao terminarmos essa verificação, alguma das duas listas vai ter elementos sobrando, pois uma acabou antes e teve todos os seus elementos appendados, então agora faremos o append desses itens que sobraram e que são os ultimos da lista por serem os maiores numeros. Como não sei qual lista acabou primeiro, então faço a verificação para as duas
    while i < len(listaA): #percorro o restante da lista A
        lista.append(listaA[i]) #e appendo cada elemento restante
        i+=1
    while j < len(listaB): #percorro o restante da lista B
        lista.append(listaB[j]) #e appendo cada elemento restante
        j+=1
    return lista #ao final retorna a lista ordenada

#O(n)

def mergesort(lista): #esse é o algoritmo que divide a lista original em sublistas, e as ordena
    if len(lista) <= 1:
        return lista
    meio = len(lista)//2
    listaA = mergesort(lista[:meio]) #vai dividindo até chegar no caso base, quando chega, chama a função do merge que ordena de fato
    listaB = mergesort(lista[meio:]) 
    return merge(listaA, listaB)

listaA = [1,18,33,42]
listaB = [2,13,16,46]
lista = merge(listaA, listaB)
print(lista)
lista = [18,1,33,42,16,46,2,13]
lista = mergesort(lista)
print(lista)


#Quick-sort - também tem as mesmas fases da divisão e conquista mas se comporta diferente em cada etapa
#Escolhe um elemento qualquer da lista e ele se torna o pivot (as matades vão até ele, < pivot e > pivot, mesmo que não sejam ordenados)

def partition(lista, esq, dir):
    r = random.randint(esq, dir)
    aux = lista[r]
    lista[r] = lista[esq]
    lista[esq] = aux
    j = esq
    pivot = lista[esq]
    for k in range(esq+1 , dir+1):
        if lista[k] < pivot:
            j+=1
            aux = lista[k]
            lista[k] = lista[j]
            lista[j] = aux
    lista[esq] = lista[j]
    lista[j] = pivot
    return j

def quicksort(lista, esq, dir):
    if esq < dir:
        p = partition(lista, esq, dir)
        quicksort(lista, esq, p-1)
        quicksort(lista, p+1, dir)
        

lista = [56,89,23,99,45,12,66,78,34]
quicksort(lista, 0, (len(lista)-1))
print(lista)

#Teorema: para qualquer entrada o tempo esperado de execução do quick-sort é O(n log n)