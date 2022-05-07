# Heranca de multi niveis e quando uma classe crianca (tambem conhecido como classe derivada)
# Herda metodos e outros atributo de outra classe crianca, isso inclui os metodos herdados
#Pela outra classe crianca


class Organismo:
#Classe vovo (mas ainda e considerada como pai do animal e do cachorro)
	vivo = True

class Animal(Organismo):
#Classe pai (mas ainda e considerada como filho do organismo)
	comida = 'Batata'
	def come(self):
		print('Esse animal esta comendo')

class Cachorro(Animal):
#Classe filho (do animal e do organismo vale ressaltar que e indiretamente)
	
	def late(self):
		self.barulho = 'Woof'
		return self.barulho


cachorro_1 = Cachorro()

print(f'Exemplo de variavel de classe herdado do classe Organismo/*avo* {cachorro_1.vivo}')

print(f'Exemplo de variavel de classe herdado da classe animal/pai {cachorro_1.comida}')

print(f'Exemplo de metodo unico para a classe cachorro {cachorro_1.late()}')