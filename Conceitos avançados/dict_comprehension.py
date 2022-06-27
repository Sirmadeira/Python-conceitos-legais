# Compreensao de dicionario = cria um dicionario se utilziando de uma expressao
#                             pode subsituir certos for loops e lambda functions
# 
# dict = {chave expression :valor expression for (chave,valor) in iteravel}
 
cidades_em_fahrenheit = {'New York': 32, 'Boston': 75, 'Rio de Janeiro': 100, 'Sampa': 50} 

cidades_em_celsius =  {k+'a' : round((v - 32)*5/9,2) for (k,v) in cidades_em_fahrenheit.items()}

print(cidades_em_celsius)


# dict = {chave: expression for (chave,valor) in iteravel if conditional }
cidades_em_brasil=  {k :v for (k,v) in cidades_em_fahrenheit.items() if k  == 'Sampa'}
print(cidades_em_brasil)
# Aplica a condicao no looop inteiro, se o k for igual a sampa voce executa senao
# Nao executa

#dict = {chave: (if/else) for (chave,valor) in iteravel}

cidades_string = {k + 'a': ('quente' if v >= 40 else 'frio') for (k,v) in cidades_em_fahrenheit.items()}
# Aplica a condicao somente no valor do dicionario um item so
print(cidades_string)


#dict = {chave: funcao() for (chave,valor) in iteravel}
def add_temp (v) -> int:
    if v:
        a = v + 15
    return a

print(cidades_temp_aumentada:={k: add_temp(v) for (k,v) in cidades_em_fahrenheit.items()})
