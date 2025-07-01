class No:
    def __init__(self, dado):
        self.dado = dado;
        self.esq = None;
        self.dir = None;
        self.cor = True;

class Arvore:
    def __init__(self):
        self.raiz = None;

    def ehVermelho(self, no):
        if no == None:
            return False;
        else:
            return no.cor == True;

    def ehPreto(self, no):
        if no == None:
            return True;
        else:
            return no.cor == False;

    def sobeVermelho(self, raiz):
        raiz.cor = True;
        raiz.esq.cor = False;
        raiz.dir.cor = False;
        return raiz;

    def rotacionaEsquerda(self, no):
        novoRaiz = no.dir;
        no.dir = novoRaiz.esq;
        novoRaiz.esq = no;
        novoRaiz.cor = no.cor;
        no.cor = True;
        return novoRaiz;
    
    def rotacionaDireita(self, no):
        novaRaiz = no.esq;
        no.esq = novaRaiz.dir;
        novaRaiz.dir = no;
        novaRaiz.cor = no.cor;
        no.cor = True;
        return novaRaiz;

    def insere_arvore(self, raiz, dado):
        if raiz == None:
            return No(dado);
        if dado < raiz.dado:
            raiz.esq = self.insere_arvore(raiz.esq, dado);
        elif dado > raiz.dado:
            raiz.dir = self.insere_arvore(raiz.dir, dado);
        else:
            return raiz;
        if self.ehPreto(raiz.esq) and self.ehVermelho(raiz.dir):
            raiz = self.rotacionaEsquerda(raiz);
        if self.ehVermelho(raiz.esq) and self.ehVermelho(raiz.esq.esq):
            raiz = self.rotacionaDireita(raiz);
        if self.ehVermelho(raiz.esq) and self.ehVermelho(raiz.dir):
            raiz = self.sobeVermelho(raiz);
        return raiz;

    def insere(self, dado):
        self.raiz = self.insere_arvore(self.raiz, dado);
        self.raiz.cor = False;
        return self.raiz;

    def busca(self, raiz, dado):
        if raiz == None:
            return None;
        else:
            if dado < raiz.dado:
                return self.busca(raiz.esq, dado);
            elif dado > raiz.dado:
                return self.busca(raiz.dir, dado);
            else:
                return raiz.dado;

if __name__ == "__main__":
    arvoreBinaria = Arvore();
    arvoreBinaria.insere(3);
    arvoreBinaria.insere(13);
    arvoreBinaria.insere(24);
    arvoreBinaria.insere(54);
    arvoreBinaria.insere(32);
    arvoreBinaria.insere(98);
    arvoreBinaria.insere(17);
    arvoreBinaria.insere(64);
    arvoreBinaria.insere(55);

    if arvoreBinaria.busca(arvoreBinaria.raiz, 13):
        print(f'numero está na arvore');
    else:
        print('não está na arvore');

    if arvoreBinaria.busca(arvoreBinaria.raiz, 22):
        print(f'numero está na arvore');
    else:
        print('não está na arvore');

    if arvoreBinaria.busca(arvoreBinaria.raiz, 24):
        print(f'numero está na arvore');
    else:
        print('não está na arvore');

    if arvoreBinaria.busca(arvoreBinaria.raiz, 99):
        print(f'numero está na arvore');
    else:
        print('não está na arvore');

    if arvoreBinaria.busca(arvoreBinaria.raiz, 123):
        print(f'numero está na arvore');
    else:
        print('não está na arvore');
