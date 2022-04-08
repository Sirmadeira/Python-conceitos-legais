# 1-A sintaxe de uma funcao funciona da seguinte maneira
def nome_da_funcao(parametros_1 : dtype do parametro) -> Dtype do que a funcao retorna

# 2-Quando voce nomeia diretamente, um parametro voce tira a necessidade. De seguir
# A ordem linear, entre eles. Exemplo:
def nome_da_funcao(parametros_1 : str,parametros_2 : str) -> Dtype do que a funcao retorna

nome_da_funcao(parametros_2 = testiculos,parametro_1 = batata) 
#  Quando voce faz a call dela voce retira a necessidade de seguir a ordem deles

#3- Voce pode forcar que um user tenha que inserir a keyword.
def nome_da_funcao(parametros_1 : str,/,parametros_2 : str) -> Dtype do que a funcao
nome_da_funcao(parametros_1 = batata, parametros_2 = testiculos ) -> Obrigatoriamente
#Forcando o retorno de keyword, usuario tem que escrever o parametros_2

#4- Forcar que um user tenha que inserir sem keyword(metodo de identificacao)
def nome_da_funcao(parametros_1 : str,*,parametros_2 : str) -> Dtype do que a funcao retorna
nome_da_funcao(parametros_1, parametros_2 ) -> Obrigatoriamente
#Forca o user a nao passar parametros_2.

#5- Voce pode ter a opcao de passar um parametro de maneira opcional, 
#isso signfica que o user nao tem que escreve-la ja que ela ja e estabelecida anteriormente
def nome_da_funcao(parametros_1 : str,*,parametros_2 : str, se_parametro3:bool=True) -> Dtype do que a funcao retorna
#No exemplo nao precisamo passar o se_parametro3, mas o user pode ainda defini-lo
nome_da_funcao(parametros_1,parametros_2,se_parametro3 = False)

#6-Voce tem a opcao de passar um array de valores, um conjunto deles de uma vez so
#Um bom exemplo para isso seria, definir uma lista antes da funcao e depois dar call
#Nessa lista dentro da sua funcao.
lista = ['batata','batata2']
def acrescenta_lista(acrescimo_a_lista :str) -> None
	lista.extend(acrescimo_a_lista)
#Exemplo da execucao da def
acrescenta_lista('batata')
#End result
print(lista)

#7- Voce nao precisa definir o seus parametros voce pode so passar um argumento 
#Chamado **extras
def nome_da_funcao(parametros_1, **extras)
	parametros_2 = extras["parametros_2"]
#Nesse caso, voce pode definir os parametros dentro da funcao
