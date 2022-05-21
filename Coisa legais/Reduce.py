# Reduce() = Aplica uma funcao a um interavel (lista, dicionario etc) e reduz ele para um valor acumulativo so.
# Executa a funcao, nos primeiros dois elementso e repete o processo ate somente um valor esta disponivel

#Exemplo de reduce

import functools

letras = ['h','e','l','l','o']

palavra = functools.reduce(lambda x , y : x + y,letras)
# Aqui podemos verificar, que ele pegou elementos da lista interou por ela toda
# E formou somente um elemento que seria a palavra
print(palavra)

factorial = [5,4,3,2,1] # 5!

numero = functools.reduce(lambda x , y : x * y, factorial)

print(numero)
# Aqui se faz a mesma coisa, pega o primeiro e segundo elemento
# Multiplica entre si
# Depois, pega o resultada da multiplicacao do primeiro
# E multiplica pelo o elemento sucessivo
# Primeiro operando
# 5*4 = 20
# Segundo operando
# 20 *3 = 60
# Terceiro operando
# 60 *2 = 120
# Ate sobrar somente um elmento, dentro do interavel.