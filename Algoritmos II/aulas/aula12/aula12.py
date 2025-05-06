import csv

def parse_percent(value):
    return float(value.strip('%'))

def parse_float(value):
    return float(value)

def carregar_dados_csv(caminho_arquivo):
    dados = []
    with open(caminho_arquivo, newline='', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile)
        cabecalho = next(leitor)
        #dados.append(cabecalho) se quiser manter o cabeÃ§alho

        for linha in leitor:
            nome = linha[0]
            roles = [r.strip() for r in linha[1].split(',')]  # ['Mid', 'Top'], por exemplo. Lista de papeis
            pickrate = parse_percent(linha[2])
            winrate = parse_percent(linha[3])
            banrate = parse_percent(linha[4])
            kills = parse_float(linha[5])
            deaths = parse_float(linha[6])
            assists = parse_float(linha[7])
            pentakills = parse_float(linha[8])

            dados.append([nome, roles, pickrate, winrate, banrate, kills, deaths, assists, pentakills])
    return dados


def countingSort(dados, dAtual):
    B = [None for _ in range(len(dados))]
    c = [0 for _ in range(10)]
    for linha in dados:
        indice = (linha[9] // (10 ** dAtual)) % 10
        c[indice] += 1
    for i in range(8, -1, -1):
        c[i] += c[i + 1]
    for i in range(len(dados)-1, -1, -1):
        linha = dados[i]
        indice = (linha[9]//(10**dAtual)) % 10
        B[c[indice]-1] = linha
        c[indice] -= 1
    return B


def RadixSort(lista, qtd):
    for d in range(0, qtd):
    #Ordena A pelo digito d (estável)
        lista = countingSort(lista, d)
    return lista

# Exemplo de uso
if __name__ == "__main__":
    dados = carregar_dados_csv('champs.csv')

    for linha in dados:
        dado = int(round((linha[5] + linha[7])/ linha[6],3)*1000)
        linha.append(dado)
    
    dados = RadixSort(dados, 4)
    for linha in dados:
        linha[9] = linha[9] / 1000
        print(str(linha[0]))