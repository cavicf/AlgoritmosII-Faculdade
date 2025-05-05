# No geral, tabelas hash são estruturas de dados fortemente recomendadas quando se precisa de uma busca rápida e eficiente.
# Isso porque, nos melhores cenários, a tabela hash realiza inserções, buscas e remoções com complexidade de tempo O(1).
# Afinal, para inserir, buscar ou remover um elemento, o índice do vetor onde a operação será realizada é calculado
# diretamente por meio da função hash, baseada em uma chave. Assim, conseguimos acessar diretamente a posição desejada,
# sem a necessidade de percorrer cada slot do vetor.
# Entretanto, a abordagem utilizada abaixo para resolver colisões — sondagem linear (Linear Probing) — pode não ser a mais adequada
# em todos os casos. Isso porque, no pior cenário, quando ocorre um *cluster* (agrupamento) de elementos em uma região da tabela,
# as operações de inserção e busca passam a ter complexidade O(n), já que é necessário verificar posição por posição até
# encontrar o slot correto.

class HashItem:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor

class HashTable:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None for slot in range(tamanho)]
        self.qtdItens = 0
    
    def funcaoHash(self, chave):
        mult = 1
        valorHash = 0
        for caractere in chave:
            valorHash += ord(caractere) * mult
            mult += 1
        return valorHash % self.tamanho

    def inserirTabela(self, chave, valor):
        dado = HashItem(chave,valor)
        indice = self.funcaoHash(dado.chave)
        #Utilizando a sondagem linear para resolver as colisões:
        while self.tabela[indice] != None and self.tabela[indice] != '*':
            if self.tabela[indice].chave == chave:
                print('item ja se econtra na tabela')
                break
            indice = (indice + 1) % self.tamanho #passa pro proximo
        if self.tabela[indice] == None or self.tabela[indice] == '*':
            self.tabela[indice] = dado
            self.qtdItens += 1
        self.checarTamanho()

    def checarTamanho(self):
        fatorCarga = self.qtdItens/self.tamanho
        if fatorCarga > 0.65:
            #dobramos o tamanho da tabela utilizando uma tabela auxiliar
            print('Fator de carga ultrapassou o limite, crescendo o tamanho da tabela...')
            novoTamanho = self.tamanho * 2
            novaTabela = HashTable(novoTamanho)
            #precisamos copiar os itens da tabela antiga para a nova então:
            for slot in range(self.tamanho):
                if self.tabela[slot] != None and self.tabela[slot] != '*': #só fazemos a cópia quando acharmos um slot que tenha algo, para não fazer cópia desenecessária de None
                    novaTabela.inserirTabela(self.tabela[slot].chave, self.tabela[slot].valor) #ao fazer isso estamos recalculando os valores hash para a nova tabela
            #agora fazemos a tabela antiga apontar pra essa nova e não perdermos a tabela original:
            self.tamanho = novoTamanho
            self.tabela = novaTabela.tabela
    
    def procurarTabela(self, chave):
        indice = self.funcaoHash(chave)
        #temos que adotar o mesmo método que usamos para inserir na busca, ou seja, fazer uma sondagem linear aqui também
        while self.tabela[indice] != None:
            if self.tabela[indice] != '*' and self.tabela[indice].chave == chave:
                print('item está na tabela!');
                return self.tabela[indice].valor
            indice = (indice + 1) % self.tamanho
        if self.tabela[indice] == None:
            print('item não está na tabela')
            return None

    def removerTabela(self, chave):
        indice = self.funcaoHash(chave)
        while self.tabela[indice] != None:
            if self.tabela[indice] != '*' and self.tabela[indice].chave == chave:
                self.tabela[indice] = '*'
                self.qtdItens -= 1
                return
            indice = (indice + 1) % self.tamanho
        if self.tabela[indice] == None:
            print('item não está na tabela')
            return None

    #com esses métodos especiais conseguimos fazer com que nossa tabela hash se comporte como um dicionario de fato, nos permitindo criar itens na tabela com um tabelaHash['nomeChave'] = valor e buscar elementos com um tabelaHash['nomeChave'].
    def __setitem__(self, chave, valor):
        self.inserirTabela(chave, valor)
    
    def __getitem__(self, chave):
        return self.procurarTabela(chave)
    
    def __delitem__(self, chave):
        return self.removerTabela(chave)
#----------------------------------------------------------------------------------------------------------------------------------
#Testando a tabela hash com linear probing pra resolver colisões
#crio uma tabela, passando seu tamanho:
tabelaHash = HashTable(13)

#inserindo valores na tabela do jeito manual;
# tabelaHash.inserirTabela('camily', 2024001197)
# tabelaHash.inserirTabela('luis', 2024001198)
# tabelaHash.inserirTabela('fernanda', 2024001199)
# tabelaHash.inserirTabela('augusto', 2024001100)
# tabelaHash.inserirTabela('julian', 2024001101)
# tabelaHash.inserirTabela('ruan', 2024001197)

#Procurando valores na tabela do jeito manual
# valor = tabelaHash.procurarTabela('fernanda')
# print(valor)
# valor = tabelaHash.procurarTabela('ruan')
# print(valor)

#Removendo item da tabela do jeito manual
# tabelaHash.removerTabela('fernanda');
# valor = tabelaHash.procurarTabela('fernanda')
# print(valor)

#Testando a tabela como se fosse um dicionario:
#inserindo
tabelaHash['camily'] = 1234
tabelaHash['jose'] = 5678
tabelaHash['zanoli'] = 9111

#buscando
print(tabelaHash['camily'])
print(tabelaHash['jose'])
print(tabelaHash['zanoli'])

#removendo
del tabelaHash['camily']
print(tabelaHash['camily'])
