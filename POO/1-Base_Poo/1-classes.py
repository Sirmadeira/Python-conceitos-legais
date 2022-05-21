# ---- Inicio ----#
# O que e um objeto ? E como se fosse algo no mundo! Tipo um microfones, uma batata
# O que e um atributo? O que um objeto uma batata tem casca.
# O que e um metodo? E o que um objeto faz, um microfone capta som
# O que e uma classe? E um diagrama que estipulas todos os atributos e metodos a serem utilizados.
class Exemplo:
# Existe uma boa pratica, em que classes tem que ter a primeira letra maiuscula
	pass
#Existe uma ideia de boa pratica, em que em grandes projetos. Voce cria modulas para a sua classe
#Basicamente uma nova file
#Nesse caso criamos um modulo chamado carros e um classe Carros. E vamos importar ela
#Aviso: Verificar a classe carros para entender melhor oq e um atributo, metodo.
from carros import Carros

carro_1=Carros(modelo='Upi',ano=2022,cor='amarelo')
carro_2=Carros(modelo='Siena',ano=2022,cor='amarelo')
#Exemplo, de objeto - Voce ve aqui, a diferenca entre classe e objeto. 
#Algo destacado pelo fato da, classe-blueprint ja ter sido executada
#Logo o objeto foi construido.
#O objeto devido, a seu constructor(__init__) precisa que voce repasse os parametros
#Para executa-lo
#Voce pode criar multiplos objetos, e eles sao totalmente independentes

print(carro_1.cor)
#Esse print demonstra o modelo do meu carro/ o meu atributo da minha classe
print(carro_1.rodas)
#Esse print demonstra o numero de rodas do meu carro / a minha variavel classe

#AVISO: Variaveis de classe podem, ser redefinidas
#Alguem que tambem pode acontecer com instancias/ atributos
carro_1.rodas = 2
print(f'Exemplo de variavel de classe sendo redefinida {carro_1.rodas}')
#Exemplo, da redefinicao da variavel de classe.
#Quando voce redefine variaveis de classe tenha cuidadao porque vode pode redefinir
#Ela para todos os outros objetos que vao vir a ser criados depois da redefinicao
Carros.rodas = 2
carro_3 = Carros(modelo='Chevrolet',ano=2022,cor = 'amarelo')
print(f'Exemplo de variavel de classe sendo redefinida para todos os objetos sucedentes{carro_3.rodas}')

print(carro_1.ano)
carro_1.pare()
#Essas linha aqui executam a acao/ executam o metodo da minha classe
