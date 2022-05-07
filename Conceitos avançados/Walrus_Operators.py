# Walrus operator :=`

# Da valor a variavel, e destaca isso.

# Fornece um valor a variavel como parte de uma expressao maior.

#Exemplo de quando ele util

happy = True
print(happy)
# Aqui e notavel, que a variavel tem q ser definido antes dela ser utilizada como um parametro
# Do metodo print.

# Com o walrus operator, e posso destacar para o python, que primeiramente ele tem que assinalar
# Um valor a variavel, antes dele executar o metodo. Ou seja, ele forca a definicao da variavel naquele
# instante. E retorna essa variavel.
print(happy:= True)


#Caso eu faco isso com o simbolo de igualdade eu tenho erro
#print(happy = True)
#Pq ele entende como se fosse umas das chaves do parametro, e nao como uma variavel sendo definida


#Exemplo do quao util ele pode ser:
# Neste exemplo, criamos com uma lista com as variaveis inseridas pelo usuario
# Caso o usuario, fale sair. A gente para essa captacao

alimentos = []

# while True:
# 	comida = input("Que comida voce quer?")
# 	if comida == 'sair':
# 		print('xauxau')
# 		break
# 	alimentos.append(comida)
# print(alimentos)
# Para dar run nesse codigo, se utiliza de interpreter.


#Exemplo de cleaner code:
#Mais zen
while comida := input('Que comida voce quer?') != 'sair':
	# Aqui estou tendo o retorno da variavel, e quando essa variavel for igual a sair
	# Eu termina o while statement
	alimentos.append(comida)
print(alimentos)