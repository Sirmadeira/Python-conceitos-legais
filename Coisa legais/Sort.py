# Sort metodo = Usado em listas
# Sorted function = Usado em interaveis, que seriam basicamente todos os tipos de colecao


nomes = ['Batata','Cenoura','Gustavo','Abril']

nomes.sort()


for i in nomes:
	print(i)
# Nesse caso estamo em ordem alfabetica
nomes.sort(reverse=True)


for i in nomes:
	print(i)
# Nesse caso estamos ordem alfabetica revertida
# Nos exemplos, acima estavamos nos utilizando do metodo unico ao objeto lista
# Caso, nos utilizasamo de outro tipo de objeto como uma tupla teriamos um errinho de AttributeError

# Se utilizando da function, sorted
# Na funcao sorted, temos um retorno em lista. No entanto, ela aceita qlqr interravel
nomes_2 = ('Batata','Cenoura','Gustavo','Abril')

nomes_tuplas = sorted(nomes_2,reverse=True)

for i in nomes_tuplas:
	print(i)
   

# As vezes os dados nao sao simples:

estudantes = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78)]

nota = lambda notas : notas[1]
idade = lambda idade: idade[2]

estudantes.sort(key = nota)

# Se estudante fosse uma tupla e nao uma lista
sorted(estudantes,key = idade)

for i in estudantes:
	print(i)