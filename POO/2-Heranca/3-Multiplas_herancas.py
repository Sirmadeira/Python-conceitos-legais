# Multipla heranca = E quando uma classe filho herda de 2 ou mais classes pai.
# Um bom exemplo e pensar na ideia, de mae e pai

class Presa:
	covarde = True
	def corre(self):
		self.distancia = '405KM'
		return self.distancia

class Predador:
	forte = True
	def morder(self):
		self.forca = '13J'
		return self.forca


class Coelho(Presa):
#Exemplo de classe com heranca unica
	pass


class Gaviao(Predador):
#Exemplo de classe com heranca unica
	pass

class Peixe(Presa,Predador):
#Exemplo de classe com multipla heranca
	pass 
	
peixe_1 = Peixe()

print(f'Esse peixe e um covarde? {peixe_1.covarde}')
#Exemplo de variavel de classe herdada de uma das classe pais(classe Presa)

peixe_2 = Peixe()

print(f'Esse peixe e forte? {peixe_2.forte}')
#Exemplo de variavel de classe herdada de uma das classe pais(classe Predador)

print(f'Meu deus o peixe_2 mordeu o peixe_1 com uma forca de {peixe_2.morder()}')
print(f'E o peixe_1 acabou correndo {peixe_1.corre()}')
#Exemplo, de como a classe peixe, consigo fazer com oq seus objetor herdassem os metodos
#Das classe pais