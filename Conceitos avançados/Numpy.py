import numpy as np

# ----- Arrays ----- #
#Um array e uma nada mais que uma matriz#
#Mas existe sub especifidades dentro dele#
# Shape - Que seria o formato da matriz#

matriz=np.array([[1,2],[2,2],[3,3]])
print(matriz.shape)


# Data type - O tipo do dado #
print(matriz.dtype) 


#Axis - Que seria o eixo analisado, barra a visualizacao que a gente tem da matriz #

# Axis = 0, a gente analisa de cima para baixo. Muito utilizado, 
#quando voce que analisar colunas ou elimina-las

# Axis = 1, a gente analisa do lado esquerdo para o lado direito,
#Muito utilizado, quando voce quer analisar linhas especificas

# ----- Vantagems - Numpy -----#
#1-E rapido
#2-Muitas funcos disponibilizadas para arrays
#3- Utilizados, em outros modulas como pandas

# ----- Usando numpy ----- #
# No uso de numpy e muito comum voce ter somente um dtype para o conteudo dentro
# Da sua coleção. E algo importante de se manter ate.
#Quando definindo seu array e um bom practice voce definir o dtype dele logo em seguida.
matriz=np.array([1,2,3,4,5],np.int64)
print(matriz.dtype)
#Quando vc se utiliza de um array voce pode converter o dtype dele para qualquer coisa.
#Cuidado obviamente, porque voce pode ter resultados inesperados.

matriz = np.array([1,2,3,4,0],np.bool8)
print(matriz.dtype)
print(matriz)
#Tal retornado, e esperado devido a ideia do codigo binario.


# ----- Metodos adicionais que criam arrays ----- #
# arange e o equivalente a funcao range
matriz = np.arange(0,12,2)

print(matriz)

#linspace- Racha o range, de acordo com o numero estabelecido no ultimo parametro

matriz = np.linspace(1,10,4)

print(matriz)

#empty- Cria um espaca de memoria para se criar um preencher um array, boa pratica
#quando preenche alguma coisa

matriz = np.empty((3,2))
print(matriz)
#Ele nao crio 0, ele nao preenche ele so abre o espaco pq ta 0 print, 
#e pq o jeito de espressar a memoria utilizada


#zero - Cria um array cheio de zeros
matriz = np.zeros((10,))
print(matriz)
#Existe outras funcoes muito semelhantes, tipo ones.
#Essa funcoes utilizadas na definicao de determinantes.

#random.metodo - Cria um array de valores random, dependendo do metodo utilizado
#Se ira ter logicas difirentes.
matriz = np.random.rand(2,7)
#So e capaz de puxar o shape do array, randomico
matriz = np.random.randint(2,7,(3,4,4))
print(matriz)

#fromiter- Pega uma interacao, que e feita em lista ou outros tipos de colecoes.
# E transforma arrayt

matriz = np.fromiter([n*n for n in range(0,10)],np.int32)
#Tbm pode se usar np.array()

print(matriz)


#----- Como dar slice em arrays ----

# Para entender o slicing em array e muito importante entendo o slicing em listas
lista = [x for x in range(0,10)]
print(lista[::-1]) 
	#Posicao de comeco#:#Uma posicao antes do final#:#Em quantos quantos pula#])
	#E assim que funfa em lista

#Mas como e que funfa em arrays?

matriz = np.random.randint(0,100,(5,7))


# Pegar as 3 primeira linhas do seu array(PEGOU tudo)
print("Batata")
print(matriz[:3])
# Nesse exemplo eu so defini o meu axis de linhas nao tudo, logo ele so rachou as linhas

# Pegar somente os elementos na visao de colunas que nao estao no inicio ou no final
print("Batata")
print(matriz[:,1:-1])
#Essa virgula racha o axis, o primeira axis e o axis 0 (que seria o das linhas)
# E ele seria oque vem antes da virgula
#O axis 1 e o das colunas e o que vem depois da virgula

# Pega os elementos de linha a cada 2 linhas e as colunas a cada 2 colunas
print("Batata")
print(matriz[::2,::2])
#Depois disso a ideia do slicing de lista ainda se aplica, principalmente no que diz step by step

# ---- Agregacoes em numpy ---- #
#Soma, media, max, min - Sao exemplo, de agregacoes
#Como fazer
print(matriz)
print(matriz[:,-3:-1].sum())
#Array que pegar somente, a quinta coluna do array, e a sexta coluna do array
#Quando voce executar essa aglomeracao ele vai colapsar o somar todos os valores dentro do array
#Se voce quiser definir se vai ser somado por coluna ou linha voce tem que definir
#O axis no metodo.
print(matriz)
print(matriz[:,-3:-1].sum(axis=0))
#Nesse caso e 0 porque eu estou querendo o somar o elemento com a linha de baixo
#Se eu quisesse somar os elementos, pela coluna do lado e escolheria o axis=1

# ---- Multiplicacao em arrays ---- #
#Em python existe duas jeitos de multiplicar alguma coisa.
#Um e se utilizando de um metodo, chamado multiply ou o caractere *
#E outro e o dot
#Primeiramente vamos exemplificar o multiply

matriz=np.array([[2,3],
				[1,5]],np.int32)

matriz2=np.array([[4,9],
				 [2,4]],np.int32)

#No multiply a gente multiplica o elemento na posicao (matriz[0,0]) com o elemento equivalente
#Na outra matriz (matriz2[0,0]).Conhecido como multiplicacao celula por celula

print(np.multiply(matriz,matriz2))


#Agora se utilizando do metodo dot voce faz basicamente multiplicacao matriz.

print(np.dot(matriz, matriz2))


#Exemplos, de multiplicacao de arrays
tabela = np.array([[2,27,5,6,83,32,86],
				  [3,21,11,6,73,44,74],
				  [1,20,9,9,68,42,69],
				  [0,19,10,9,58,36,67],
				  [4,20,6,12,68,50,66]])  

#Pontos ganhos de acordo
pontos = np.array([3,1,0])
#E um vetor, esse vetor e ao mesmo tempo uma coluna quanto uma linha.

#Subset dos jogos jogados (tabela[:,1]=Vitorias,tabela[:,2]=Empates,tabela[:,3]=Derrotas)
print(tabela[:,1:4])

print(pontos)
#Nesse exemplo, temos uma tabela com o numero de colunas igual 
#a o numero de eventos dentro do vetor(3,0 ou 0,3) colunas e linhas sao a mesma coisa
#Aqui fazemos a multiplicacao de matriz
pontos_totais=np.dot(tabela[:,1:4],pontos)
print(pontos_totais)
#Vemos que temos exatamente, o resultado que queriamos. 
#Algo causado pela equivalencia destacada anteriormente
#No exemplo, abaixo temos a multiplicacao celula por celula
pontos_rachados=np.multiply(tabela[:,1:4],pontos)
print(pontos_rachados)
#Nesse casos ele me da dissociado, o total de pontos dividido entre (vitoria 0,x/empate 1,x/derrota 2,x)
print(pontos_rachados.sum(axis=1))
#Para obter o total de uma vez

# ---- Sorting arrays ---- #

tabela = np.array([[2,27,5,6,83,32,86],
				  [3,21,11,6,73,44,74],
				  [1,20,9,9,68,42,69],
				  [0,19,10,9,58,36,67],
				  [4,20,6,12,68,50,66]]) 


tabela_ordenada = np.sort(tabela,axis=0)
print(tabela_ordenada)
#Metodo utilizado para ordenar, a tabela. Se voce nao inserir nenhum parametro 
#Voce vai ter um resultado inesperado, ele vai auto definir o axis e vai provalvemente
#Executar algo que voce nao queria q acontecesse, vale ressaltar que esse metodo
#Ele se utiliza de todas as linhas ou colunas como index, o que acaba misturando tudo
#Basicamente nao se manteve um index de posicao, unico


#Como organizar de maneira que uma coluna qualquer seja index?
#Voce vai se utilizar de um metodo chamado argsort, para encontrar o index pela qual voce quer
#Organizar
tabela_ordenada_index = np.argsort(tabela[:,2])
#Ele vai retornar um vetor que diz a ordem em que os indexes vao ser organizados
#0 e igual ao primeira carinha da tabela [2,27,5,6,83,32,86]
#4 e igual ao quarto index da tabela [4,20,6,12,68,50,66]
#E assim vai indo
#Exemplo, de vetor de indexes
print(tabela_ordenada_index)
#E aqui esta o resultado final
#Como se utilizar desse vetor? Se utilizar de slice
tabela_organizado_pela_segunda_coluna = tabela[tabela_ordenada_index]
print(tabela_organizado_pela_segunda_coluna)


# ---- Como dar join entre arrays ---- #

tabela = np.array([[2,27,5,6,83,32,86],
				  [3,21,11,6,73,44,74],
				  [1,20,9,9,68,42,69],
				  [0,19,10,9,58,36,67],
				  [4,20,6,12,68,50,66]]) 



tabela2 = np.array([[2,27,5,6,83,32,86],
				  [3,21,11,6,73,44,74],
				  [1,20,9,9,68,42,69],
				  [0,19,10,9,58,36,67],
				  [4,20,6,12,68,50,66]])

#Geralmente, voce quer por um dataset em cima do outro
#Ex:
				  # [2,27,5,6,83,32,86],
				  # [3,21,11,6,73,44,74],
				  # [1,20,9,9,68,42,69],
				  # [0,19,10,9,58,36,67],
				  # [4,20,6,12,68,50,66],
				  # [2,27,5,6,83,32,86],
				  # [3,21,11,6,73,44,74],
				  # [1,20,9,9,68,42,69],
				  # [0,19,10,9,58,36,67],
				  # [4,20,6,12,68,50,66]
#Vamos aprender a fazer isso
#Para isso se utilizamos de um metodo chamado stack

combinado = np.stack([tabela,tabela2],0)
#Passa as duas tabelas que voce quer stackar. E o axis pelo qual voce quer stackar
#Nesse caso, voce associo os arrays, mas eles nao foram juntados necessariamente
#Ele so vai deixar os arrays, em pacotinhos. Ou melhor so vai criar mais uma dimensao.
#Resultado final
print(combinado)
print(combinado.shape)
#Mas agora como colar eles
colado = np.concatenate([tabela,tabela2],axis=0)
print(colado)


# ---- Finalizando (metodos interessantes) e adicionais---- #


tabela = np.array([[2,27,5,6,83,32,86],
				  [3,21,11,6,73,44,74],
				  [1,20,9,9,68,42,69],
				  [0,19,10,9,58,36,67],
				  [4,20,6,12,68,50,66]]) 


#Filtering : 'Mostra somente os elementos que atendem a condicao'

testes = tabela >=80
#Isso daki so vai mostrar os locais do array em que condicao foi verdadeira
print(testes)
#Mas e caso voce queira ver os verdadeiro valores e nao um monte de true false?
#Isso daki vai retornar todos os valores, verdadeiros do array
tabela_filtrada = tabela[testes]
print(tabela_filtrada)

#transpose: Inverte o shape do array (Linhas viram colunas e colunas viram linhas)
tabela_transposado = tabela.T
tabela_transposado = np.transpose(tabela)
print(tabela_transposado)
#Flatten: Transforma o array em vetor
#Nesse voce vai ver que a colecao array ja tem o metodo adendo a ela
print(tabela.flatten())
#Existe um metodo mais rapido conhecido como ravel, que executa a mesma coisa
#So que e um pouquinho nao muito utilizado
print(np.ravel(tabela))

#Como editar o seu array
tabela[0][0] = 22
print(tabela)

#Como dar reshape, o remodelar o seu array
tabela_moldada= tabela.reshape((35))
print(tabela_moldada)
# Resize e a mesma coisa so que ele perdoa mais, mas ele tambem destroi o seu array muitas vezes
tabela_moldada= np.resize(tabela,(4,4))
print(tabela_moldada)
#Clipe

nova_tabela = tabela.clip(10,50)

print(nova_tabela)