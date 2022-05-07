# Funcoes de ordem maior = Seria uma funcao que tem a capacidade de receber uma funcao
# Ou retornar uma. No python, isso dae e possivel porque funcoes tambem sao objetos


def alto(texto:str) -> str:
	return texto.upper()

def baixo(texto:str) -> str:
	return texto.lower()

def ola(function):
	texto = function('BaTata')
	print(texto)

ola(alto)



