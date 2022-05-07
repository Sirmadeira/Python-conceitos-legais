# --- Inicio --- #
# Heranca, e a ideia de deixar algo.
# Em classes esse conceito e aplicavel
# Voce tem uma classe pai, que pode deixar algum tipo de heranca para seus filhos
# Esses filhos sao conhecidos como subclasses
# Uma classe filho, so consegue herdar metodos e variaveis de classe nunca atributos.
# --- Porque usar -- #
# Nos utilizamos, de heranca para n repetir codigo. 
#Basicamente, qnd herdamos nao temos que definir novamente um metodo 
#Ou uma variavel de classe, na classe filho. Sendo que o pai ja tem.
#E alem do mais quando alteramos algo na classe pai, os filhos herdam tambem essas mudancas

class Animal:
#Exemplo de classe pai
	
	vivo = True

	def come(self):
		print("Esse animal esta comendo")

	def dormir(self):
		print("Esse animal esta dormindo")

class Coelho(Animal):
# Exemplo de classe filho, voce ve que e necessario por entre parenteses o nome da classe pai

	def correr(self):
		print("Esse coelho esta correndo")

class Peixe(Animal):
	def nadar(self):
		print("Esse peixa esta correndo")



print(f'Exemplo de variavel de classe herdada pela subclasse {Coelho.vivo}')
#EXemplo de como uma classe filho herda a variavel classe

coelho_1=Coelho()

print(f'Exemplo de metodo/acao herdada da classe pai')
coelho_1.come()
# Exemplo de como uma classe filho herda um metodo


print(f'Exemplo de metodos unicos para as classe filhos')
coelho_1.correr()

print(f'Exemplo de como o metodo e  unico somente para o filho')
#coelho_1.nadar()
#Isso daki da erro, pq e suposto