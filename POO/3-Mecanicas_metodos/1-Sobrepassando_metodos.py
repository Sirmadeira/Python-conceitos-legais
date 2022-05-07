class Animal:
	def comer(self):
		self.comida = 'carne'
		return f'O animal comeu {self.comida}'

class Coelho(Animal):
	pass


Coelho_1 = Coelho()
print(f'{Coelho_1.comer()}')
#Exemplo de como a classe coelho, ta tendo um metodo que ela nao quis herdar
#Nesse caso, o coelho esta comendo carne
# --- Inicio --- #
#Para evitar ocasioes desse tipo nos utilizamo de metodos_sobrepassados
#Onde substituimos um metodo herdado pro um natural da classe

class Coelho_correto(Animal):
	# Para sobrepassar um metodo herdado temos que seguir a mesma assinatura dele
	#A assinatura do metodo, seria o nome dele em conjunto com os parametro passados
	def comer(self):
		#Exemplo de assinatura do metodo herdado, sendo sobrepassada
		self.comida = 'Cenoura'
		return f'O animal comeu {self.comida}'

Coelho_2 = Coelho_correto()

print(f'Exemplo, de classe com um metodo herdado sobrepassado {Coelho_2.comer()}')
