# filter() = Cria uma collecao de elementos de um interavel.Em que uma funcao aplicada e verdadeira
#filter(function,iterable)
# Returna um filtered object, basicamente um conjunto de verdadeira ou falsos
# Que sao definidos de acordo, com a condicao estipulada

friends = [("Rachel",19),
           ("Monica",18),
           ("Phoebe",17),
           ("Joey",16),
           ("Chandler",21),
           ("Ross",20)]

idade = lambda idade : idade[1] < 20
# Nesse caso o chandley na entra na condicao logo ele nao e retornado

print(list(filter(idade,friends)))