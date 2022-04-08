# ----- Lambda e uma funcao anonima ----- #
#Basicamente, uma funcao que nao tem nome#
#E so e capaz de ter um retorno #
#Exemplo:

cubo = (lambda x: x**3)

print(cubo(4))

#Em funcao anonimas, voce pode ter duis parametros ou mais somadas

soma_nome=(lambda primeiro_nome, segundo_nome : primeiro_nome + ' ' + segundo_nome)

#A funcao acima em funcao normal.

def soma_nome(primeiro_nome:str,segundo_nome:str) -> str:
	return primeiro_nome + ' ' + segundo_nome

print(soma_nome('Batata','BATATA'))


