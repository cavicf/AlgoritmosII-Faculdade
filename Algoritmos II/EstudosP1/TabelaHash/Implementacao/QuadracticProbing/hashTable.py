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

#A abordagem utilizada abaixo para resolver colisões — sondagem quadrática (Quadractic Probing) — pode não ser a mais adequada
# em todos os casos também. Isso porque apesar de não formar mais agrupamentos sucessivos na tabela, o padrão de sondagem é fixo e, ao ocorrer colisões, os dados serão inseridos de forma padronizada pois o incremento para a próxima posição de indice é o mesmo para todas as chaves que possuirem o mesmo valor hash e isso pode gerar um *cluster* (agrupamento) secundário de elementos em uma sequencia padronizada de slots. No pior caso, com a tabela completamente cheia, as operações de inserção e busca passam a ter complexidade O(n), já que é necessário verificar posições suceesivas padronizadas até encontrar o slot correto. Mesmo com o fator de carga sendo controlado e, portanto o pior cenário da tabela estar completamente cheia não poder existir, essa formação de clusters pode fazer com que até em análise de caso médio as operações assumam complexidade de O(n)
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
                if self.tabela[slot] != None and self.tabela[slot] != '*':
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
            #Utilizando quadractic probing para resolver as colisões:
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
            #Utilizando quadractic probing para percorrer as colisões:
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
            #Utilizando quadractic probing para percorrer as colisões:
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
