#Implementação do bubble-sort 
#ele é um algoritmo estavel por sua natureza de trocar elementos adjacentes, da esquerda pra direita então o que aparece primeiro será colocado antes do que o que aparece depois e eles não trocam entre si, pois a troca só ocorre se o elemento da esquerda for estritamente maior ou menor que o da direita

def bubbleSort(lista):
    ultimoIndice = len(lista) - 1 #é o ultimo indice da minha lista que vai de 0 até n-1
    trocou = False #uso a flag do trocou para que caso meu algoritmo receba um vetor já ordenado, ele faça apenas uma iteração de comparações pra verificar se trocou algo ou não
    for i in range(ultimoIndice, -1, -1): #vai até -1 pq para em 0, o -1 não conta, portanto fazendo isso estou percorrendo n elementos
        for j in range(0, i, 1):
            if lista[j][1] > lista[j+1][1]:
                lista[j], lista[j+1] = lista[j+1], lista[j] #troca os elementos 
                trocou = True
        if trocou == False:
            break


#Testando o bubble-Sort
lista = [('camily', 20), ('jose', 50), ('pedro', 2), ('rafael', 27), ('rodrigo', 50), ('julia', 20)]
bubbleSort(lista);
print(lista)
