#vamos usar o counting sort pra ordenar os digitos do menos significativo para o mais significativo

def countingSort(lista, digitoAtual):
    listaContagem = [0 for _ in range(0, 10)] #a lista com a contagem é limitada de 0 a 9 visto que os algorismos podem variar de 0 a 9 apenas
    listaOrdenada = [None for _ in range(0, len(lista))]
    for item in lista:
        indice = (item[1]//10**digitoAtual) % 10
        listaContagem[indice] += 1
    for i in range(1, 10):
        listaContagem[i] += listaContagem[i-1]
    for i in range(len(lista)-1, -1, -1):
        atual = lista[i]
        indice = (atual[1]//10**digitoAtual) % 10
        listaOrdenada[listaContagem[indice] - 1] = atual
        listaContagem[indice] -= 1
    return listaOrdenada

def radixSort(lista, qtdDigitos):
    for digito in range(0, qtdDigitos):
        lista = countingSort(lista, digito)
    return lista

lista = [('camily', 2), ('jose', 2), ('pedro', 2), ('rafael', 1)]
lista = radixSort(lista, 1)
print(lista)