# Duck typing e basicamente um conceito de se escrever codigo orientado a objeto, 
# No qual, se da muito mais valor
# Aos metodos e atributos de uma classe, do que sobre a classe em si
# Basicamente, damos mais valor ao que uma classe faz e tem como caracteristica
# Do que sobre o que a classe diz que ela e. O que significa, que nao checamos
# O tipo de classe, causa ela tenhos os atributos e metodos minimos
# Vem do popular ditado:
# Se anda como um pato, tem penas como um pato provalvemente e um pato.


class Pato:
	def andar(self):
		print('Esse pato esta andando')

	def falar(self):
		print('Esse pato esta quackando')


class Galinha:
	def andar(self):
		print('Essa galinha esta andando')

	def falar(self):
		print('Essa galinha esta fazendo piu')


class Pessoa:
	def pegar_o_animal(self,animal):
		animal.andar()
		animal.falar()
		# Exemplo de como, as classes passado nao tem o seu tipo classe verificado
		# Podemos nos utilizar de ambas delas, contanto que elas tenham os atributos necessarios ou
		# Os metodos
		print('Parabens voce pegou o animal!')

pato_1 = Pato()
galinha_1 = Galinha()
pessoa_1 = Pessoa()

pessoa_1.pegar_o_animal(pato_1)