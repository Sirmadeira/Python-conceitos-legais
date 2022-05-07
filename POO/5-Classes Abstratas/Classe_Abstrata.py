# Porque se utilizar de classe abstrata?
# Ela e mais utilizada como template ou um exemplo de como um codigo tem que ser desenvolvido
# Ela previne que o usuarios construa um objeto daquela classe
# Ela impede a classe filho de herdar os metodos abstratos da classe abstrata

# O que e uma classe abstrata?
# Classe abstrata = E uma classe, que contem metodos abstratos

# Metodo abstrato = E um metodo que e declarado (tem nome etc), mas nao ele nao e implementado


from abc import ABC, abstractmethod
#Possibilita o usu de classe abstratas


class Veiculo(ABC):
	#Para poder ser uma classe abstrata ela tem que herdar da classe ABC
	#Exemplo, de classe abstrata

	@abstractmethod
	#Esse decorator faz com que a classe e o metodo se tornem abstratos 
	def andar(self):
		#Exemplo, de metodo abstrato
		#Se o metodo abstrato nao tiver o decorator, a classe deixa de ser abstrata
		#E a gente pode criar um objeto com ela.
		pass
	@abstractmethod
	def parar(self):
		pass 


class Carro(Veiculo):
	def andar(self):
		print('Voce esta dirigindo um carro')
	def para(self):
		print('Voce esta parando o seu carro')
		# Ela tambem obriga, todas as classe filhos a sobrepassar(dar override) nos metodos abstratos definidos na classe pai.
		# Entao no exemplo, acima ao criarmos um objeto, da classe carro.
		# Seriamos obrigado, a sobrepassar o metodo parar. 
		# Ou seja, obrigamos o user a definir os metodo dados pelo template(classe abstrata)
		# Se o nao fizermos, teriamos um erro


class Motocicleta(Veiculo):
	pass

#veiculo_1 = Veiculo()
#Exemplo: De como a classe abstrata nao pode criar metodos.

#Motocicleta_1 = Motocicleta()
#Exemplo: De como a classe abstratra caso seja pai, impede que a classe filho se utilize dela
