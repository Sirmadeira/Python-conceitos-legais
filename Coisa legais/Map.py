# Map = Aplica uma funcao a cada item de um interavel(tupla,lista, etc.)
# Retorna um map object
# Map(function,iterable)

store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]


para_euro = lambda data : (data[0],data[1]*0.82)
# Essa funcao tem a abilidade de multiplicar o item no index 1 por 0.82

#print(list(map(para_euro,store)))
#Quando nos utilizamos da map aqui, aplicamos essa funcao em ciam da nossa data


store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

pega_numero = lambda dados : dados[1]

print(list(map(pega_numero,store)))
