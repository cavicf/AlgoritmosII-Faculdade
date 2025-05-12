#Ordenação Linear
#A entrada desse problema de ordenação são inteiros de 0 até K
#Com esse tipo de entrada espicifica, conseguimos um algoritmo com complexidade de O(n+k)
#Mas se definimos um limite para K, teremos uma constante multiplicada por n, que resulta em O(n) para o algoritmo
#Um algoritmo conhecido pra isso é o: 

#Counting Sort
#A ideia geral dela 

k=8
lista = [3,4,2,1,8,0]

c = [0 for _ in range(0, k+1)]
for a in lista:
    c[a] += 1

for i in range(1, k+1):
    c[i] = c[i] + c[i-1]

B = [None for _ in range(0, len(lista))]
for a in lista:
    B[c[a]-1] = a

print(B)

#isso é uma ordenação instavel, pois não respeita a ordem dos elementos repetidos
# def countingSort(lista, k):
#     c = [0 for _ in range(0, k+1)]
#     B = [None for _ in range(0, len(lista))]
#     for a in lista:
#         c[a] += 1
#     for i in range(1, k+1):
#         c[i] = c[i] + c[i-1]
#     for a in lista:
#         B[c[a]-1] = a
#         c[a] -= 1
#     return B

#Essa é a versão estável, que respeita a ordem dos elementos repetidos
def countingSort(lista, k):
    c = [0 for _ in range(0, k+1)]
    B = [None for _ in range(0, len(lista))]
    for a in lista:
        c[a] += 1
    for i in range(1, k+1):
        c[i] = c[i] + c[i-1]
    for i in range(len(lista)-1, -1, -1):
        a = lista[i]
        B[c[a]-1] = a
        c[a] -= 1
    return B
 
lista2 = [3,3,4,2,1,8,0,1]
list = countingSort(lista2, 8)
print(list)