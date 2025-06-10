import random
import sys
sys.setrecursionlimit(1000000)

class node:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None
    
def insere(y, dado):
    if y is None: # Use 'is None' for checking None
        return node(dado)
        
    if dado < y.dado:
        y.esq = insere(y.esq, dado) 
    elif dado > y.dado:
        y.dir = insere(y.dir, dado)     
    else:
        #print("dado igual")
        # tratar esse caso
        return y # Return y when dado is equal to prevent infinite recursion
    return y 

def busca(T, dado):
    if T is None: # Use 'is None' for checking None
        return None
    if dado < T.dado:
        return busca(T.esq, dado)
    elif dado > T.dado:
        return busca(T.dir, dado)
    else:
        return T 

# Main execution part
T = None
operacoes = int(sys.argv[1])
for i in range(operacoes):
    T = insere(T, i)

for i in range(operacoes):
    resultado = busca(T, i)
    # You might want to print 'resultado' or do something with it here
    # For example:
    # if resultado:
    #     print(f"Found {i} in the tree.")
    # else:
    #     print(f"{i} not found.")