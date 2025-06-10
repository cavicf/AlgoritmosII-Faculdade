#Arvores AVL - Criadores Adelson, Vesky e Landis
#Pode ter os mesmos problemas da rubro negra de inserção em ordem que pode gerar um lista ligada
#Começa com o calculo do FATOR DE BALANCEAMENTO da arvore que consiste na altura da arvore esquerda - a altura da arvore direita
#FB = hesq - hdir
#O fator de balanceamento de qualquer nó tem que estar entre [-1, 0, 1]
#Uma avores vazia tem altura -1 
#Um nó sozinho sem filhos tem altura 0
#Se a inserção for nos filhos extremos uma rotação basta pra corrigir
#se for feita uma inserção nos nós internos precisa de mais de uma rotação

class node:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None
        self.altura = 0

def altura(no):
    if no == None:
        return -1
    return no.altura

def rotacaoDireita(raiz):
    novaRaiz = raiz.esq
    raiz.esq = novaRaiz.dir
    novaRaiz.dir = raiz
    raiz.altura = max(altura(novaRaiz.esq), altura(novaRaiz.dir)) + 1
    novaRaiz.altura = max(altura(novaRaiz.esq), altura(novaRaiz.dir)) + 1
    return novaRaiz

def rotacaoEsquerda(raiz):
    novaRaiz = raiz.dir
    raiz.dir = novaRaiz.esq
    novaRaiz.esq = raiz
    raiz.altura = max(altura(novaRaiz.esq), altura(novaRaiz.dir)) + 1
    novaRaiz.altura = max(altura(novaRaiz.esq), altura(novaRaiz.dir)) + 1
    return novaRaiz

def fb(no):
    return altura(no.esq) - altura(no.dir)

def insere(raiz, dado):
    if raiz == None:
        return node(dado)
    if dado < raiz.dado:
        raiz.esq = insere(raiz.esq, dado)
        if fb(raiz) == 2:
            if dado > raiz.esq.dado:
                #inseriu na direita da esquerda
                raiz.esq = rotacaoEsquerda(raiz.esq)
            raiz = rotacaoDireita(raiz)
    elif dado > raiz.dado:
        raiz.dir = insere(raiz.dir, dado)
        if fb(raiz) == -2:
            if dado < raiz.dir.dado:
                #inseriu na esquerda da direita
                raiz.dir = rotacaoDireita(raiz.dir)
            raiz = rotacaoEsquerda(raiz)
    else:
        print('dado ja existe')
        return raiz
    raiz.altura = max(altura(raiz.esq), altura(raiz.dir)) + 1
    return raiz

