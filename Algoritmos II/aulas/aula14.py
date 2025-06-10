class No:
    def __init__(self, dado):
        self.dado = dado
        self.esquerdo = None
        self.direito = None
        self.cor = True #indica q tem cor e é vermelho, se for false é negro

def rotacionaEsquerda(raiz):
    novaRaiz = raiz.direito    
    raiz.direito = novaRaiz.esquerdo
    novaRaiz.esquerdo = raiz
    novaRaiz.cor = raiz.cor
    raiz.cor = True
    return novaRaiz

def rotacionaDireita(raiz):
    novaRaiz = raiz.esquerdo
    raiz.esquerdo = novaRaiz.direito
    novaRaiz.direito = raiz
    novaRaiz = raiz.cor
    raiz.cor = True
    return novaRaiz

def sobeVermelho(raiz):
    raiz.cor = True
    raiz.esquerdo.cor = False
    raiz.direito.cor = False

def eVermelho(no):
    if no == None:
        return False
    return no.cor

def eNegro(no):
    if no == None:
        return True
    return no.cor == False

def insere(raiz, dado):
    if raiz == None:
        return No(dado)
    elif dado < raiz.dado:
        raiz.esquerdo = insere(raiz.esquerdo, dado)
    elif dado > raiz.dado:
        raiz.direito = insere(raiz.direiro, dado)
    else:
        return raiz
    if eVermelho(raiz.direito) and eNegro(raiz.esquerdo):
        raiz = rotacionaEsquerda(raiz)
    if eVermelho(raiz.esquerdo) and eVermelho(raiz.esquerdo.esquerdo):
        raiz = rotacionaDireita(raiz)
    if eVermelho(raiz.esquerdo) and eVermelho(raiz.direito):
        sobeVermelho(raiz)
    return raiz

def insere_arvore(raiz, dado):
    raiz = insere(raiz, dado)
    raiz.cor = False
    return raiz

def imprime(arvore):
    if arvore == None:
        return
    print('(', end='')
    imprime(arvore.esquerdo)
    print(',', end='')
    print(arvore.dado, end='')
    imprime(arvore.direito)
    print(')', end='')

arvore = No(5)
arvore.direito = No(7)
arvore = rotacionaEsquerda(arvore)
imprime(arvore)
arvore = rotacionaDireita(arvore)
imprime(arvore)
print()


#Propriedades adicionais da rubro negra, fora as comuns de arvore binaria de busca:
#Todo nó possui uma cor: negro ou vermelho
#Nó vermelho é filho esquerdo do pai
#Raiz é negra
#Todo nó vermelho possui filhos negros
#Arvores vazias(folhas) são negras (Nones)
#Mais importante: Para qualquer nó que pegarmos da arvore, a distancia para qualquer folha descendente dele passa pelo mesmo número de nós negros, ou seja, mesma altura de filhos negros (altura negra).