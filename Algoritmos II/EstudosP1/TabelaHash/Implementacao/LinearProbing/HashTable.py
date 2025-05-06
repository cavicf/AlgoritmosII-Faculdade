# No geral, tabelas hash são estruturas de dados fortemente recomendadas quando se precisa de uma busca rápida e eficiente.
# Isso porque, nos melhores cenários, a tabela hash realiza inserções, buscas e remoções com complexidade de tempo O(1).
# Afinal, para inserir, buscar ou remover um elemento, o índice do vetor onde a operação será realizada é calculado
# diretamente por meio da função hash, baseada em uma chave. Assim, conseguimos acessar diretamente a posição desejada,
# sem a necessidade de percorrer cada slot do vetor.
#Entretanto, não é possível a existencia de uma função hash perfeita que garanta uma distribuição uniforme e diferente para cada chave que queremos inserir na tabela, e devido a isso, ocorrem as chamadas colisões.
#Colisões ocorrem quando dadas diferentes chaves, a função hash produz a mesma saída para todas elas, ou seja, todas as chaves tentarão ser colocadas no mesmos indice da tabela. Existem algumas estratégias para se contornar e lidar com essa colisões.
#As duas estratégias mais populares são a de endereçamento aberto e endereçamento fechado.
#Endereçamento aberto se refere a ideia de que quando vamos inserir um novo dado na tabela, se ocorrer uma colisão com outro elemento ja presente na tabela, procuramos o próximo slot disponível da tabela para inserir esse dado. Essa técnica também é conhecida como 'hashing fechado' pois não saímos da tabela para tratar as colisões, cada dado é inserido em uma posição de indice dado pela função hash. Existem 3 principais técnicas de calcular esse próximo slot disponivel da tabela: linear probing (sondagem linear), quadractic probing(sondagem quadrática) e double hashing(dispersão dupla).
#Endereçamento fechado se refere a ideia de que, independentemente de ocorrer uma colisão em um indice fornecido pela função hash, vamos armazenar todos os dados naqula mesma posição, ou seja, permitimos que multiplos dados possuam o mesmo valor hash. Isso é possível adotando a estratégia de colocar em cada slot da tabela, uma outra estrutura de dados capazes de armazenar todas as ocorrencias de dados no indice fornecido pela função hash. Essa técnica também é conhecida como 'hashing aberto', pois não inserimos os dados na posição de indice da tabela, mas sim saímos dessa posição de indice para inserir esse dado em uma outra estrutura.Existem muitas técnicas e estruturas que podemos escolher para inserir essas ocorrencias de colisões, sendo as mais conhecidas: Encadeamento (cada slot da tabela possui uma lista encadeada), vetores (cada slot da tabela possui uma lista comum) e arvores binarias de busca (cada slot da tabela possui uma arvore binaria de busca). 
#Vale ressaltar que a adoção de diferentes técnicas causam diferentes comportamentos na tabela, fazendo com que na análise de pior caso, possamos ter resultados diferentes de complexidade 

#A abordagem utilizada abaixo para resolver colisões — sondagem linear (Linear Probing) — pode não ser a mais adequada em todos os casos. Isso porque, ao ocorrer colisões, os dados serão inseridos sucessivamente na tabela, gerando clusters (agrupamento) de elementos em uma região da tabela. Na análise de pior caso, quando a tabela estiver totalmente cheia, as operações de inserção e busca passam a ter complexidade O(n), já que é necessário verificar posição por posição até encontrar o slot correto. Mesmo com o fator de carga sendo controlado e, portanto o pior cenário da tabela estar completamente cheia não poder existir, essa formação de clusters pode fazer com que até em análise de caso médio as operações assumam complexidade de O(n)
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
