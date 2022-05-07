# Corrente_metodos = Seria a chamada de multiplos metodo/acoes sequencialmente
#					 cada chamada retorna uma acao/metodo diferente no mesmo objeto
#                    Vale ressaltar que tambem retorna self


class Carro:
	
	def ligar(self):
		print('O carro ligou!')
		return self

	def dirigir(self):
		print('Voce esta dirigindo o carro')
		return self

	def desligar(self):
		print('Voce desligou o carro')
		return self


Carro_1 = Carro()

Carro_1.ligar().dirigir()
#Aviso: Qnd o metodo nao retorna nada ele vai retornar
		# O valor None (vazio)
		#Por isso, qnd usamos corrente de metodos
		#Geralmente, retornamo o argumento self
		#Que seria nada mais do que um jeito de rechamar a seu objeto
		#Para entender melhor, quando o metodo tem return self
		#Ele faria isso daki
		#Carro_1.ligar().Carro_1().dirigir()
		#Aviso: Isso daki da erro ta mas pense desse jeito

Carro_1.ligar()\
	   .dirigir()\
	   .desligar()
# Um bom jeito, de tornar corrente metodos mais legiveis seria o uso desse tipo de sintaxe
#Nesse caso, o backslash significa continuacao de linha de codigo




