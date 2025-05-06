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

#A abordagem utilizada abaixo — Double Hashing — é geralmente considerada a mais eficiente entre as técnicas de endereçamento aberto, pois o incremento usado para sondagem depende de uma segunda função hash aplicada à chave. Diferente da sondagem linear e quadrática, cujo padrão de sondagem é fixo ou previsível, o Double Hashing gera sequências de sondagem diferentes para chaves distintas, o que evita a formação de clusters e melhora a distribuição dos dados na tabela. Assim, mesmo com um fator de carga razoável, a complexidade média de inserção, busca e remoção permanece O(1), ao passo que nas outras técnicas ainda pode haver piora para O(n) devido à formação de agrupamentos de dados.
class HashItem:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor

class HashTable:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela =[None for slots in range(self.tamanho)]
        self.qtdItens = 0

    def funcaoHash1(self, chave):
        indice = 0
        multiplicador = 1
        for caractere in chave:
            indice += ord(caractere) * multiplicador
            multiplicador += 1
        return indice % self.tamanho

    def funcaoHash2(self, chave):
        indice = 0
        multiplicador = 1
        for caractere in chave:
            indice += ord(caractere) * multiplicador
            multiplicador += 1
        return indice

    def checarTamanho(self):
        fatorCarga = self.qtdItens / self.tamanho
        if fatorCarga > 0.65:
            tabelaAuxiliar = HashTable(self.tamanho * 2)
            for slot in range(self.tamanho):
                if self.tabela[slot] != None and self.tabela[slot] != '*':
                    tabelaAuxiliar.inserirTabela(self.tabela[slot].chave, self.tabela[slot].valor)
            self.tamanho = self.tamanho * 2
            self.tabela = tabelaAuxiliar.tabela
    
    def inserirTabela(self, chave, valor):
        dado = HashItem(chave, valor)
        somador = 1
        indice = self.funcaoHash1(chave)
        while self.tabela[indice] != None and self.tabela[indice] != '*':
            if self.tabela[indice].chave == dado.chave:
                print('item ja está na tabela')
                break
            #Utilizando double hashing para resolver as colisões:
            indice = (indice + somador * (5 - (self.funcaoHash2(dado.chave) % 5))) % self.tamanho
            somador += 1
        if self.tabela[indice] == None or self.tabela[indice] == '*':
            self.tabela[indice] = dado
            self.qtdItens += 1

    def procurarTabela(self, chave):
        indice = self.funcaoHash1(chave)
        somador = 1
        while self.tabela[indice] != None:
            if self.tabela[indice] != '*' and self.tabela[indice].chave == chave:
                print(f'{chave} está na tabela')
                return self.tabela[indice].valor
            #Utilizando double hashing para percorrer as colisões:
            indice = (indice + somador * (5 - (self.funcaoHash2(chave) % 5))) % self.tamanho
            somador += 1
        if self.tabela[indice] == None:
            print(f'{chave} não existe na tabela')
            return None

    def removerTabela(self, chave):
        indice = self.funcaoHash1(chave)
        somador = 1
        while self.tabela[indice] != None:
            if self.tabela[indice] != '*' and self.tabela[indice].chave == chave:
                self.tabela[indice] = '*'
                print(f'removendo o dado {chave} da tabela')
                return
            #Utilizando double hashing para percorrer as colisões:
            indice = (indice + somador * (5 - (self.funcaoHash2(chave) % 5))) % self.tamanho
            somador += 1
        if self.tabela[indice] == None:
            print(f'o dado {chave} ja não existia na tabela')
    
    def __setitem__(self, chave, valor):
        self.inserirTabela(chave, valor)
    
    def __getitem__(self, chave):
        return self.procurarTabela(chave)

    def __delitem__(self, chave):
        return self.removerTabela(chave)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#Testando a tabela hash com double Hashing

tabelaHash = HashTable(13)

tabelaHash['camily'] = 1234
tabelaHash['jose'] = 5678
tabelaHash['zanoli'] = 9111

print(tabelaHash['camily'])
print(tabelaHash['jose'])
print(tabelaHash['joao'])

del tabelaHash['jose']
print(tabelaHash['jose'])

del tabelaHash['cintia']