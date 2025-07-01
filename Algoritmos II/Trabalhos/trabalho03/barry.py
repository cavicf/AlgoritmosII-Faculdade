#Camily Victal Finamor - 2024001197
#Luis Gustavo Riso Santos - 2024002372

import random
import time
MINIMO = 1
MAXIMO = 9_223_372_036_854_775_807
random.seed(42)  

ESTOU_SUBMETENDO_NO_RUNCODES = True

#Implementação utilizando a Rubro Negra Esquerdsta
class noh:
  def __init__(self, dado):
    self.dado = dado
    self.esq = None
    self.dir = None
    self.cor = True

def ehVermelho(no):
  if no == None:
    return False
  else:
    return no.cor == True
  
def ehPreto(no):
  if no == None:
    return True
  else:
    return no.cor == False
  
def subirVermelho(no):
  no.cor = True
  no.esq.cor = False
  no.dir.cor = False
  return no

def rotacionaEsquerda(no):
  novoNo = no.dir
  no.dir = novoNo.esq
  novoNo.esq = no
  novoNo.cor = no.cor
  no.cor = True
  return novoNo

def rotacionaDireita(no):
  novoNo = no.esq
  no.esq = novoNo.dir
  novoNo.dir = no
  novoNo.cor = no.cor
  no.cor = True
  return novoNo

def insereArvore(raiz, dado):
  if raiz == None:
    return noh(dado)
  if dado < raiz.dado:
    raiz.esq = insereArvore(raiz.esq, dado)
  elif dado > raiz.dado:
    raiz.dir = insereArvore(raiz.dir, dado)
  else:
    return raiz
  if ehPreto(raiz.esq) and ehVermelho(raiz.dir):
    raiz = rotacionaEsquerda(raiz)
  if ehVermelho(raiz.esq) and ehVermelho(raiz.esq.esq):
    raiz = rotacionaDireita(raiz)
  if ehVermelho(raiz.esq) and ehVermelho(raiz.dir):
    raiz = subirVermelho(raiz)
  return raiz
  
def insere(raiz, dado):
  raiz = insereArvore(raiz,dado)
  raiz.cor = False
  return raiz
  
def em_ordem(no):
  if no == None:
    return
  em_ordem(no.esq)
  print(no.dado)
  em_ordem(no.dir) 
  
def encontra_mais_proximo(no, x):
  valorMaisProximo = no.dado
  melhorDistancia = abs(no.dado - x)
  atual = no
  while atual != None:
    distanciaAtual = abs(atual.dado - x)
    if distanciaAtual < melhorDistancia:
      valorMaisProximo = atual.dado
      melhorDistancia = distanciaAtual
    elif distanciaAtual == melhorDistancia:
      if atual.dado < valorMaisProximo:
        valorMaisProximo = atual.dado
        melhorDistancia = distanciaAtual
    if x < atual.dado:
      atual = atual.esq
    elif x > atual.dado:
      atual = atual.dir
    else:
      return atual.dado
  return valorMaisProximo

def inicializa_arvore(n):
  numeros = random.sample(range(MINIMO, MAXIMO), n)
  numeros.sort()
  raiz = None
  for num in numeros:
    raiz = insere(raiz, num)
  return raiz

def insere_novos_numeros(arvore, n):
  numeros = random.sample(range(MINIMO, MAXIMO), n)
  for num in numeros:
    arvore = insere(arvore, num)
  return arvore


nivel = int(input("Digite o nivel do jogo 1-fácil, 2-normal, 3-difícil, 4-insano: "))
if nivel == 1:
  MAXIMO = 100
  n = 5
elif nivel == 2:
  MAXIMO = 1000
  n = 100
elif nivel == 3:
  n = 5
else:
  n = 50000

arvore = inicializa_arvore(n)
print("\nNúmeros inseridos no jogo:")
if not ESTOU_SUBMETENDO_NO_RUNCODES:
  em_ordem(arvore)
x = random.randint(MINIMO, MAXIMO)
print(f"\n\nQual o valor mais próximo de {x} digite -1 para sair:")

inicio = time.time()
chute = int(input(""))
print()
while chute >= 0:
  mais_proximo = encontra_mais_proximo(arvore, x)
  if chute == mais_proximo:
    fim = time.time()
    tempo = fim - inicio
    print(f"Parabéns! Você acertou! O número mais próximo de {x} é {mais_proximo}.")
    if not ESTOU_SUBMETENDO_NO_RUNCODES:
      print(f"Você levou {tempo:.2f} segundos.")
    arvore = insere_novos_numeros(arvore, 3)
    
    if not ESTOU_SUBMETENDO_NO_RUNCODES:
      print("\n**************************")
      print("Números inseridos no jogo:")
      em_ordem(arvore)
    x = random.randint(MINIMO, MAXIMO)
    print(f"\n\nQual o valor mais próximo de {x}:")
    inicio = time.time()
    chute = int(input(""))
  else:
    chute = int(input(f"\nErrou! {chute} não é a resposta!\nTente novamente: "))

print("Saindo!")  