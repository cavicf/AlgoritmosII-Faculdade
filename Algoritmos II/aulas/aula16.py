import matplotlib.pyplot as plt
import random

# FunÃ§Ã£o gerada pelo ChatGPT :)
def desenhar_arvore(raiz):
    """
    Desenha a Ã¡rvore binÃ¡ria usando matplotlib, com nÃ³s e texto maiores.
    """
    fig, ax = plt.subplots(figsize=(16, 12))  # Tamanho grande
    ax.axis('off')

    # Define the recursive helper function inside, so it can access ax directly
    def _desenhar(node, x, y, dx):
        if node is None:
            return

        # Desenhar o nÃ³ com texto e cÃ­rculo maiores
        ax.text(
            x, y, str(node.dado),
            ha='center', va='center',
            fontsize=16,  # Tamanho do texto
            bbox=dict(boxstyle="circle,pad=0.6", facecolor='lightblue', edgecolor='black', linewidth=1.5)
        )

        # Desenhar linha e chamada recursiva para o filho esquerdo
        if node.esq:
            nx, ny = x - dx, y - 1.5
            ax.plot([x, nx], [y, ny], 'k-', linewidth=1.5)
            _desenhar(node.esq, nx, ny, dx / 2)

        # Desenhar linha e chamada recursiva para o filho direito
        if node.dir:
            nx, ny = x + dx, y - 1.5
            ax.plot([x, nx], [y, ny], 'k-', linewidth=1.5)
            _desenhar(node.dir, nx, ny, dx / 2)

    _desenhar(raiz, x=0, y=0, dx=8)
    plt.show()

# --- Rest of your AVL tree code (assuming it's already correctly indented) ---

class node:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None
        self.altura = 0

def altura(y):
    if y is None:
        return -1
    return y.altura

def rotacaoDireita(y):
    x = y.esq
    y.esq = x.dir
    x.dir = y

    y.altura = max(altura(y.esq), altura(y.dir)) + 1
    x.altura = max(altura(x.esq), altura(x.dir)) + 1

    return x

def rotacaoEsquerda(y):
    x = y.dir
    y.dir = x.esq
    x.esq = y

    y.altura = max(altura(y.esq), altura(y.dir)) + 1
    x.altura = max(altura(x.esq), altura(x.dir)) + 1

    return x

# FB = FATOR DE BALANCEAMENTO
def fb(y):
    return altura(y.esq) - altura(y.dir)

def insere(y, dado):
    if y is None:
        return node(dado)

    if dado < y.dado:
        y.esq = insere(y.esq, dado)
        if fb(y) == 2:
            if dado > y.esq.dado:
                y.esq = rotacaoEsquerda(y.esq)
            y = rotacaoDireita(y)
    elif dado > y.dado:
        y.dir = insere(y.dir, dado)
        if fb(y) == -2:
            if dado < y.dir.dado:
                y.dir = rotacaoDireita(y.dir)
            y = rotacaoEsquerda(y)
    else:
        print("dado igual")
        return y

    y.altura = max(altura(y.dir), altura(y.esq)) + 1
    return y

def busca(T, dado):
    if T is None:
        return None
    if dado < T.dado:
        return busca(T.esq, dado)
    elif dado > T.dado:
        return busca(T.dir, dado)
    else:
        return T

# Main execution part
T = None
valor = input("Digite um valor para inserir (ou vazio para parar): ")
while valor != '':
    T = insere(T, int(valor))
    desenhar_arvore(T)
    valor = input("Digite um valor para inserir (ou vazio para parar): ")