class Maxheap:
    def __init__(self, lista): #recebe a lista de dados a ser ordenada
        self.dados = lista #colocamos ela em um auxiliar
        self.tamanho = len(lista) #pegamos o tamanho dela
        self.constroiHeap() #E chamamos a função que ira reorganizar essa lista em uma max-heap valida, ou seja, onde os pais são sempre maiores que os filhos

    def constroiHeap(self):
        for i in range((self.tamanho //2) - 1, -1 ,-1): #assumimos que as folhas da arvore ja são heaps, então pegamos o ultimo nó mais a esquerda q possui filhos
            self.desceHeap(i) #e verficamos se esse elemento pai, é de fato maior que seus filhos, e se não, precisamos desce-lo

    def sobeHeap(self, i):
        if i == 0: #
            return
        pai = (i-1) // 2
        if self.dados[i] > self.dados[pai]:
            self.dados[i], self.dados[pai] = self.dados[pai], self.dados[i] #faz a troca dos elementos de lugar
            self.sobeHeap(pai)

    #sempre vai inserir o mais a esquerda o possível
    def inserir(self, valor):
        self.dados.append(valor) #ao adicionar o novo elemento, eu posso ferir a regra de o pai ser sempre maior q os filhos, então precisamos reorganizar
        self.tamanho += 1
        self.sobeHeap(self.tamanho - 1) #passa o ultimo elemento para a função que é o indice do ultimo elemento
        
    def desceHeap(self, i): #dado o nó pai 
        esq = 2*i + 1 #calculamos em que indice da lista estão seu filho esquerdo
        dir = 2*i+2 #e seu filho direito
        maior = -1 #iniciamos a variavel maior com um valor arbitrario só para podermos armazenar o maior valor encontrado nela 
        if esq <= self.tamanho - 1: #verifico se esse nó esquerdo existe, ou seja, se esse indice está dentro dos limites da lista
            maior = esq #se estiver, primeiro digo que o filho esquerdo é o maior
        if dir <= self.tamanho - 1 and self.dados[dir] > self.dados[esq]: #então verificamos se o filho direito existe, e se ele existir, comparamos os dados desses indices
            maior = dir #se o direito for maior, então dizemos que o maior falor entre os filhos é o direito
        if maior != -1 and self.dados[maior] > self.dados[i]:  #verifico se existiram filhos pro nó pai que estamos verificando, ou seja, a variavel maior só vai receber um valor se existir 
            #um filho direito ou esquerdo. Então comparamos o valor do maior filho que encontramos com o valor do nó pai
            self.dados[i], self.dados[maior] = self.dados[maior], self.dados[i] #se ele for maior, trocamos ele com o nó pai 
            self.desceHeap(maior) #e agora no indice maior, esta o antigo pai, e caso esse nó tenha filhos, precisamos verificar se ele não está violando as regras com seus filhos também, por
            #isso chamamos recursivamente nele, para garantir q esteja tudo organizado.

    def remover(self): #para remover o nó raiz precisamos fazer algumas operações
        if self.tamanho == 0: #se o tamanho da lista for 0, quer dizer que ja ordenamos todos os nós e acabou a ordenação
            return None #então retornamos none
        maximo = self.dados[0] #agora se ainda tem elementos, eu guardo o primeiro valor da minha lista, pois sei que é o meu valor maximo que quero inserir na lista ordenada
        self.dados[0] = self.dados[self.tamanho - 1] #e passo o ultimo valor da minha arvore para a primeira posição
        self.dados.pop() #removo esse elemento por completo da lista
        self.tamanho -= 1 #diminuo o tamanho pois removemos um elemento
        if self.tamanho > 0: #se ainda houver elementos na minha lista, chamo o desce heap para manter minha heap valida depois que colocamos o ultimo elemento como a raiz
            self.desceHeap(0)
        return maximo #depois disso devolvo esse maximo pra inserir na minha lista ordenada

#Vamos utilizar o heap para extrair o maior para colocar na ultima posição da lista com o selection sort
#Tem complexidade O(nlogn) e não precisa de memória auxiliar, então é muito bom, mas suas constantes são maiores
    def HeapSort(self):
        for i in range(self.tamanho - 1, 0, -1): #percorro minha lista ao contrario, pois o max heap sempre retorna o maior valor, então quero inseri-los ao fim da minha lista
            self.dados[0], self.dados[i] = self.dados[i], self.dados[0] #então troco meu primeiro item (maior valor), com a posição atual da lista que estamos ordenando
            self.tamanho -= 1 #diminuo o tamanho pois significa que um item ja está ordenado após essa operação
            self.desceHeap(0) #então chamo o desceheap para reorganizar minha arvore heap e manter ela valida.

L = [18, 1, 6, 33, 42, 31]
H = Maxheap(L)
H.HeapSort()
print(H.dados)
