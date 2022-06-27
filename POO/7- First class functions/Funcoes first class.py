# Funcoes first class = Seria um conceito python onde a funcao e tratada como um objeto
# Isso fornece uma serie de boosts por assim dizer. Ou mecanicas interessantes
# Algumas utilidades sao:

# 1- Podemos arquivar uma funcao nao executada em uma variavel
def alto(texto:str) -> str:
	return texto.upper()

var_funcao = alto('oi')

#2- Elas podem ser utilizadas como argumentos de outras funcoes 

def ola(function):
	# Function convencao necessaria para passar funcoes como argumento
	texto = function('BaTata')
	print(texto)

ola(alto)

#3- Funcoes podem retornar outras funcoes


def funcao_fora(msg):
    messagem = msg
    # Variavel livre - Seria basicamente, uma variavel que tambem e utilizavel pela funcao_dentro()
    # Muito semelhante, ao  conceito de variavel de classe
    def funcao_dentro():
        print(messagem)
    return funcao_dentro
