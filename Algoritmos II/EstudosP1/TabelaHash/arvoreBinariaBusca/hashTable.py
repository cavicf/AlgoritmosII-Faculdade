# No geral, tabelas hash são estruturas de dados fortemente recomendadas quando se precisa de uma busca rápida e eficiente.
# Isso porque, nos melhores cenários, a tabela hash realiza inserções, buscas e remoções com complexidade de tempo O(1).
# Afinal, para inserir, buscar ou remover um elemento, o índice do vetor onde a operação será realizada é calculado
# diretamente por meio da função hash, baseada em uma chave. Assim, conseguimos acessar diretamente a posição desejada,
# sem a necessidade de percorrer cada slot do vetor.
#Entretanto, não é possível a existencia de uma função hash perfeita que garanta uma distribuição uniforme e diferente para cada chave que queremos inserir na tabela, e devido a isso, ocorrem as chamadas colisões.
#Colisões ocorrem quando dadas diferentes chaves, a função hash produz a mesma saída para todas elas, ou seja, todas as chaves tentarão ser colocadas no mesmos indice da tabela. Existem algumas estratégias para se contornar e lidar com essa colisões.
#As duas estratégias mais populares são a de endereçamento aberto e endereçamento fechado.
#Endereçamento aberto se refere a ideia de que quando vamos inserir um novo dado na tabela, se ocorrer uma colisão com outro elemento ja presente na tabela, procuramos o próximo slot disponível da tabela para inserir esse dado. Essa técnica também é conhecida como 'hashing fechado' pois não saímos da tabela para tratar as colisões, cada dado é inserido em uma posição de indice dado pela função hash. Existem 3 principais técnicas de calcular esse próximo slot disponivel da tabela: linear probing (sondagem linear), quadractic probing(sondagem quadrática) e double hashing(dispersão dupla).
#Endereçamento fechado se refere a ideia de que, independentemente de ocorrer uma colisão em um indice fornecido pela função hash, vamos armazenar todos os dados naqula mesma posição, ou seja, permitimos que multiplos dados possuam o mesmo valor hash. Isso é possível adotando a estratégia de colocar em cada slot da tabela, uma outra estrutura de dados capazes de armazenar todas as ocorrencias de dados no indice fornecido pela função hash. Essa técnica também é conhecida como 'hashing aberto', pois não inserimos os dados na posição de indice da tabela, mas sim saímos dessa posição de indice para inserir esse dado em uma outra estrutura.Existem muitas técnicas e estruturas que podemos escolher para inserir essas ocorrencias de colisões, sendo as mais conhecidas: Encadeamento (cada slot da tabela possui uma lista encadeada), vetores (cada slot da tabela possui uma lista comum) e arvores binarias de busca (cada slot da tabela possui uma arvore binaria de busca). Esse tipo de abordagem é vantajosa, pois a quantidade de slots na tabela não define a quantidade de itens que podem ser inseridos na tabela, pois cada slot pode guardar tantos elementos quanto necessesário
#Vale ressaltar que a adoção de diferentes técnicas causam diferentes comportamentos na tabela, fazendo com que na análise de pior caso, possamos ter resultados diferentes de complexidade 

# A abordagem utilizada abaixo é uma técnica de endereçamento fechado com árvore binária de busca (ABB) — onde cada slot da tabela possui uma árvore para tratar colisões. Essa técnica é considerada uma das melhores formas de endereçamento fechado, pois, ao utilizar uma ABB, suas operações de busca apresentam complexidade média de O(log n), o que é significativamente melhor em comparação às soluções baseadas em listas encadeadas ou vetores.
# No pior caso, todos os dados podem colidir em um único slot e, se a árvore não for balanceada, ela pode degenerar em uma lista encadeada, resultando em complexidade O(n). No entanto, em casos médios, a árvore tende a se manter razoavelmente balanceada, preservando a eficiência de O(log n) para buscas.
# Esse desempenho ocorre porque, a cada passo da busca, a ABB elimina metade dos elementos não relevantes, reduzindo consideravelmente o tempo necessário para localizar um item.

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