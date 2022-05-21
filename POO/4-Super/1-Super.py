# Super = E uma funcao que da acesso aos metodos da classe pai.
#         Retorna um objeto temporario, de uma classe pai qnd usada.


#Exemplo, de quando o metodo super e utilizado
class Retangulo:
	def __init__(self,comprimento,largura):
		self.comprimento = comprimento
		self.largura = largura
		

class Quadrado(Retangulo):
	def __init__(self,largura,comprimento):
		super().__init__(comprimento,largura)
		#Aqui a gente, acaba destacando para todo mundo que le esse codigo
		#Que estamos pegando um metodo, especifico da classe pai
		#Para evitar formar outro metodo(__init__) que seria igual ao metodo init do pai
		#IMPORTANTE: E tambem, para possibilitar a heranca dos ATRIBUTOS
		#Sintaxe:
		#(chamado do metodo super).(funcao a herdar(com o seus parametros obrigatorios/nao precisa self))
	def area(self):
		return self.comprimento*self.largura

class Cubo(Retangulo):
	def __init__(self,largura,comprimento,altura):
		super().__init__(comprimento,largura)
		self.altura	 = altura

	def volume(self):
		return self.comprimento*self.largura*self.altura


Quadrado_1 = Quadrado(3,3)

Cubo_1 = Cubo(3,3,3)

print(Cubo_1.volume())
print(Quadrado_1.area())