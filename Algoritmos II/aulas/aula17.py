#Arvore B é uma generalização da arvore binaria que conhecemos, mas no lugar do nó ter apenas um dado, ele pode ter varios, podendo então ter varios filhos no lugar de apenas dois. A arvore B reduz os acessos no disco, tem uma altura menor
#Tem como desvantagem uma dificuldade na busca pois mesmo que chegue em um nó, ainda n tem garantia de que o dado procurado está lá
#A quantidade de chaves aceitável em um nó está entre 50 a 2000
#A ideia é que em cada nó colocaremos a quantidade de chaves correspondentes de um bloco do hd.

#Propriedades da Arvore B
# 1 - cada nó tem um atributo de numero inteiro que indica o numero de chaves que serão armazenadas naquele nó
    # a - as chaves tem que estar em ordem crescente. Ex: damos um nome pra chave, x.key0 < x.key1 < x.key/n-1
    # b - Devemos guardar um booleano chamado de leaf(folha) que diz se aquele nó é uma folha ou não
# 2 - Cada nó interno x tem xn+1 apontadores pra filhos, ou n+1 filhos x.c0, x.x1 etc
# 3 - Se ki é uma chave em x.ci então k0 < x.key0 < k1 < x.key1 , ou seja, os filhos de uma chave tem que ser valores que são menores, entre o maiores que os nós pais
# 4 - todas as folhas tem a mesma profundidade (altura H da arvore), ou seja, todas as folhas estão a mesma distancia da raiz 
# 5 - Dado um inteiro t, todo nó, exceto a raiz, tem pelo menos t-1 chaves e t filhos se não for uma folha
# No máximo 2t-1 chaves e 2t filhos é a quantidade que cabe em um nó

#Definição: um nó é dito cheio se tem 2t-1 chaves

#um nó, exceto a raiz, tem pelo menos t-1 chaves (e t filhos), e no máximo 2t-1 chaves (e 2t filhos)
t = 3

class node:
    def __init__(self):
        self.n = 0
        self.folha = True
        self.chaves = []
        self.filhos = []

#Devolve o valor se encontrar, se não devolve None
def busca(arvore, valor):
    if arvore == None:
        return None #Se a arvore estiver vazia no inicio da busca
    i = 0 
    while i < arvore.n and valor > arvore.chaves[i]:
        i += 1
    #se tiver está no filho i, ou é a própria chave[i]
    if i < arvore.n and valor == arvore.chaves[i]:
        return arvore.chaves[i]
    elif arvore.folha == True:
        return None
    else:
        return busca(arvore.filhos[i], valor)

    # cada no, exceto a raiz, tem pelo menos t-1 chaves
# e no máximo 2t-1 chaves e 2t filhos

def quebrar_filho(pai, indiceFilho):
    novoNo = node()
    filhoQuebrar = pai.filhos[indiceFilho]
    novoNo.folha = filhoQuebrar.folha
    pai.chaves.insert(indiceFilho, filhoQuebrar.chaves[t-1])
    novoNo.chaves = filhoQuebrar.chaves[t:]
    filhoQuebrar.chaves = filhoQuebrar.chaves[:t-1]
    pai.filhos.insert(indiceFilho + 1, novoNo)
    if not filhoQuebrar.folha:
        novoNo.filhos = filhoQuebrar.filhos[t:]
        filhoQuebrar = filhoQuebrar.filhos[:t]
    pai.n = pai.n + 1
    filhoQuebrar.n = t-1
    novoNo.n = t-1

def insere_nao_cheio(x, k):
    if x.folha:
      i = 0
      while i < x.n and x.chaves[i] < k:
         i+=1
         x.chaves.insert(i, k)
         x.n = x.n + 1
    else:
        i = 0
        while i < x.n and x.chaves[i] < k:
           i+=1
        if x.filhos[i].n == 2 * t-1:
            quebrar_filho(x, i)
            if x.chaves[i] < k:
               i += 1
        insere_nao_cheio(x.filhos[i], k)

    

def imprime_arvore(raiz, nivel=0):
  for i in range(nivel):
    print("  ", end="")
  print(raiz.chaves)
  for filho in raiz.filhos:
    imprime_arvore(filho, nivel + 1)


def quebrar_raiz(raiz):
   novaRaiz = node()
   novaRaiz.folha = False
   novaRaiz.n = 0
   novaRaiz.filhos.append(raiz)
   quebrar_filho(novaRaiz, 0)
   return novaRaiz

def insere(raiz, dado):
    if raiz.n == 2 * t -1:
        raiz.quebrar_raiz(raiz)
    insere_nao_cheio(raiz, dado)
    return raiz

arvore = node()
arvore.chaves = [100, 200]
arvore.n = 2
arvore.folha = False
arvore.filhos = [node(), node(), node()]

arvore.filhos[0].folha = True
arvore.filhos[0].n = 5
arvore.filhos[0].chaves = [1, 6, 18, 33, 42]

arvore.filhos[1].folha = True
arvore.filhos[1].n = 3
arvore.filhos[1].chaves = [150, 175, 180]

arvore.filhos[2].folha = True
arvore.filhos[2].n = 2
arvore.filhos[2].chaves = [250, 275]
insere_nao_cheio(arvore, 5)
insere_nao_cheio(arvore, 4)
insere_nao_cheio(arvore, 3)
insere_nao_cheio(arvore, 2)
insere_nao_cheio(arvore, 7)
insere_nao_cheio(arvore, 8)
insere_nao_cheio(arvore, 9)
insere_nao_cheio(arvore, 10)
arvore = quebrar_raiz(arvore)

insere(arvore, 11)
insere(arvore, 12)
insere(arvore, 13)
insere(arvore, 14)
insere(arvore, 15)
insere(arvore, 16)
insere(arvore, 17)
insere(arvore, 19)
insere(arvore, 20)
insere(arvore, 151)
insere(arvore, 152)
insere(arvore, 153)
insere(arvore, 154)





imprime_arvore(arvore)
quebrar_filho(arvore, 0)


