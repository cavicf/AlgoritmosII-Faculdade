class HashItem:
    def __init__(self, chave, valor):
        self.chave = chave 
        self.valor = valor

class HashTable:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None for slots in range(self.tamanho)]
        self.qtdItens = 0

    def funcaoHash(self, chave):
        indice = 0
        multiplicador = 1
        for caractere in chave:
            indice += ord(caractere) * multiplicador
            multiplicador += 1
        return indice % self.tamanho
    
    def checarTamanho(self):
        fatorCarga = self.qtdItens / self.tamanho
        if fatorCarga > 0.65:
            tabelaAuxiliar = HashTable(self.tamanho * 2)
            for slot in range(self.tamanho):
                if self.tabela[slot] != None:
                    tabelaAuxiliar.inserirTabela(self.tabela[slot].chave, self.tabela[slot].valor)
            self.tamanho = self.tamanho * 2
            self.tabela = tabelaAuxiliar.tabela
    
    def inserirTabela(self, chave, valor):
        dado = HashItem(chave, valor)
        indice = self.funcaoHash(dado.chave)
        polinomio = 1
        while self.tabela[indice] != None and self.tabela[indice] != '*':
            if dado.chave == self.tabela[indice].chave:
                print('Item ja se encontra na tabela!')
                break
            indice = (indice + polinomio*polinomio) % self.tamanho
            polinomio += 1
        if self.tabela[indice] == None or self.tabela[indice] == '*':
            self.tabela[indice] = dado
            self.qtdItens += 1
            self.checarTamanho()

    def procurarTabela(self, chave):
        indice = self.funcaoHash(chave)
        polinomio = 1
        while self.tabela[indice] != None:
            if self.tabela[indice] != '*' and self.tabela[indice].chave == chave:
                print(f'o item {chave} está na tabela')
                return self.tabela[indice].valor
            indice = (indice + polinomio * polinomio) % self.tamanho
            polinomio += 1
        if self.tabela[indice] == None:
            print('item não existe na tabela')
            return None
        
    def removerTabela(self, chave):
        indice = self.funcaoHash(chave)
        polinomio = 1
        while self.tabela[indice] != None:
            if self.tabela[indice] != '*' and self.tabela[indice].chave == chave:
                self.tabela[indice] = '*'
                print('Item excluido')
                self.qtdItens -= 1
                return
            indice = (indice + polinomio * polinomio) % self.tamanho
            polinomio += 1
        if self.tabela[indice] == None:
            print('item não está na tabela')
            return None

    
    def __setitem__(self, chave, valor):
        self.inserirTabela(chave, valor)

    def __getitem__(self, chave):
        return self.procurarTabela(chave)
    
    def __delitem__(self, chave):
        return self.removerTabela(chave)

#------------------------------------------------------------------------------------------------------------------------
#Testando a tabela como se ela fosse um dicionario 

tabelaHash = HashTable(13)

tabelaHash['camily'] = 1234
tabelaHash['jose'] = 5678
tabelaHash['zanoli'] = 9111

print(tabelaHash['camily'])
print(tabelaHash['jose'])
print(tabelaHash['joao'])

del tabelaHash['jose']
print(tabelaHash['jose'])
