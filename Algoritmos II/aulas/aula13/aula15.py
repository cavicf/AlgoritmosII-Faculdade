class HashTable:
	def __init__(self, size):
		self.size = size
		self.slots = [[] for i in range(size)]
		
	def hash(self, s):
		mult = 1
		hash_value = 0
		for c in s[:3]: #pega só os tres primeiros caracteres 
			c = c.lower()
			hash_value += (123**mult) * ord(c)
			mult += 1
		return hash_value
		
	def put(self, key):
		hv = self.hash(key[1]) % self.size
		#supor que todo put é diferente
		self.slots[hv].append((key))
	
	def get(self, key):
		hv = self.hash(key) % self.size
		for k in self.slots[hv]:
			if key[:3] == k[1][:3]:
				return self.slots[hv]
		return None

#----------------------------------------------------------------------------------------------------------------------------
Table = HashTable(997)

def alteraString(nome):
	alterado = ''
	for c in nome[:3]:
		c = c.lower()
		match c:
			case '4' | '@':
				alterado += 'a'
			case '3':
				alterado += 'e'
			case '1' | '!':
				alterado += 'i'
			case '0':
				alterado += 'o'
			case '5' | '$':
				alterado+= 's'
			case '#':
				alterado +='h'
			case '<' | 'x':
				alterado += 'k'
			case _:
				alterado += c
	alterado += nome[3:]
	return alterado


nomes_invocadores = []

with open("invocadores.txt", "r", encoding="utf-8") as arquivo:
	for linha in arquivo:
		nome = linha.strip()  # Remove espaços em branco e quebras de linha
		if nome:  # Garante que não adiciona linhas vazias
			alterado = alteraString(nome)
			Table.put((nome, alterado))

nome_busca = input()

while nome_busca != "-1":
    nome_busca = alteraString(nome_busca)
    resultado = Table.get(nome_busca)
    if resultado:
        string = nome_busca[:3]
        for c in resultado:
            if c[1][:3] == string:
                print(f"Nome encontrado: {c[0]}")
    else:
        print("Nome não encontrado.")
    nome_busca = input()



	
"""
'a': ['4', '@'],
'e': ['3'],
'i': ['1', '!'],
'o': ['0'],
's': ['5', '$'],
'h': ['#'],
'k': ['<', 'x'],
"""