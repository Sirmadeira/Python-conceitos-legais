# 1-A sintaxe de uma funcao funciona da seguinte maneira
def nome_da_funcao(parametros_1 : dtype do parametro) -> Dtype do que a funcao retorna

# 2-Quando voce nomeia diretamente, um parametro voce tira a necessidade. De seguir
# A ordem linear, entre eles. Exemplo:
def nome_da_funcao(parametros_1 : str,parametros_2 : str) -> Dtype do que a funcao retorna

nome_da_funcao(parametros_2 = testiculos,parametro_1 = batata) 
#  Quando voce faz a call dela voce retira a necessidade de seguir a ordem deles

#3- Voce pode forcar que um user tenha que inserir a keyword ou nao.
def nome_da_funcao(parametros_1 : str,/,parametros_2 : str) -> Dtype do que a funcao retorna
#Forcando o retorno de keyword, usuario tem que escrever o nome
#4- Forcar que um user tenha que inserir sem keyword
def nome_da_funcao(parametros_1 : str,*,parametros_2 : str) -> Dtype do que a funcao retorna
#Forca o user a nao passar keywords