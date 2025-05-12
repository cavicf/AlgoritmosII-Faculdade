def insertionSort(lista):
    for i in range(1, len(lista)):
        j = i
        valor = lista[i]
        while j>0 and lista[i][1] < lista[j-1][1]:
            lista[j] = lista[j-1]
            j-=1
        lista[j] = valor
        
def bucketSort(lista):
    tamanho = len(lista)
    buckets = [[] for _ in range(tamanho)]
    for numero in lista:
        indice = int(numero[1]*tamanho)
        buckets[indice].append(numero)
    for lis in buckets:
        insertionSort(lis)
    indice = 0
    for lis in buckets:
        for numeros in lis:
            lista[indice] = numeros
            indice+=1 
    
lista = [('camily', 0.24), ('jose', 0.24), ('pedro', 0.5), ('rafael', 0.45)]
bucketSort(lista)
print(lista)