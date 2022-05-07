class Carros:
	#Variaveis de classe sao variaveis definidas fora do contructor (__init__)
	#Geralmente, conhecidas pela fato de ser constantes, em todos os objetos que vao ser contruidos
	#No exemplo, um carro sempre tem quatro rodas.
	rodas = 4
	#Exemplo de variavel de classe, variaveis de classe geralmente tem valores default
	def __init__(self,modelo:str,ano:int,cor:str):
		#Esse metodo dunder significa inicializacao, 
		#Ele seria o nosso contrutor ou melhor o cara que faz o objeto.
		#Ele e muito utilizado para se passar os atributos necessarios para construir a nossa classe
		#E para tornar cada objeto criado unico. Afinal atributos/caracteristicas diferentes carros diferentes
		self.modelo = modelo # As variaveis definidas	
		  					 # dentro do contructor (__init__), sao chamadas de instancias
		self.ano = ano 		 # Exemplo de instancia, geralmente definidas pelo user
		self.cor = cor       
		#Exemplos de atributos, tambem.
		#Existe um padrao, de se utilizar self, quando o atributo se refere ao objeto

	def dirigir(self):
		#Self - Refere ao objeto que usa esse metodo
		#Nesse caso, seria objeto Carros, que sera contruido na nossa main file(classes)
		#Vale ressaltar, que o argumento self nao precisa ser definido
		#Porque ele so e um jeito de destacar ou referir o objeto.
		print(f'O carro {self.modelo} esta andando!')
	def pare(self):
		print(f'O carro {self.modelo} esta parando!')
