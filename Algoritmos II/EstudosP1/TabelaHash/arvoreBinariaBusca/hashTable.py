class Node:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.direito = None
        self.esquerdo = None
        
class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserirArvore(self, chave, valor):
        no = Node(chave, valor)
        if self.raiz == None:
            self.raiz = no
        else:
            noAtual = self.raiz
            anterior = None
            while noAtual != None:
                anterior = noAtual
                if no.chave < anterior.chave:
                    noAtual = noAtual.esquerdo
                    if noAtual == None:
                        anterior.esquerdo = no
                        break
                else:
                    noAtual = noAtual.direito
                    if noAtual == None:
                        anterior.direito = no
                        break
        
    def buscarArvore(self, chave):
        if self.raiz == None:
            print('não existem itens nesse slot')
            return None
        else:
            noAtual = self.raiz
            while noAtual != None:
                if noAtual.chave == chave:
                    print(f'{chave} está na tabela e vale:')
                    return noAtual.valor
                else:
                    if chave < noAtual.chave:
                        noAtual = noAtual.esquerdo
                    else: 
                        noAtual = noAtual.direito
            if noAtual == None:
                print('Item não está na arvore')
                return None
#--------------------------------------------------------------------------------------------------------------------------------

class HashTable:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [ArvoreBinaria() for slot in range(self.tamanho)]
        self.qtdItens = 0
    
    def funcaoHash(self, chave):
        indice = 0
        multiplicador = 1
        for caractere in chave:
            indice += ord(caractere) * multiplicador
            multiplicador += 1
        return indice % self.tamanho
    
    def inserirTabela(self, chave, valor):
        indice = self.funcaoHash(chave)
        self.tabela[indice].inserirArvore(chave, valor)

    def procurarTabela(self, chave):
        indice = self.funcaoHash(chave)
        return self.tabela[indice].buscarArvore(chave)
    
    def __setitem__(self, chave, valor):
        self.inserirTabela(chave, valor)

    def __getitem__(self, chave):
        return self.procurarTabela(chave)
    

#----------------------------------------------------------------------------------------------------------------------------------
#Testando a tabela hash com vetor pra resolver colisões
#crio uma tabela, passando seu tamanho:
tabelaHash = HashTable(13)


tabelaHash['camily'] = 1234
tabelaHash['jose'] = 5678
tabelaHash['zanoli'] = 9111

#buscando
print(tabelaHash['camily'])
print(tabelaHash['jose'])
print(tabelaHash['zanoli'])

print(tabelaHash['camilz'])