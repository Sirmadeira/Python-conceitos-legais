# Quando geralmente fazemos isso?
# Quando desejamos alterar algum elemento do objeto produzido pela classe
# E tambem quando utilizamos de duck typing (proxima aula)


class Carro:
	cor = None
	# Variavel de classe

class Motocicleta:
	cor = None


def altera_cor(veiculo,cor:str) -> object:

	veiculo.cor = cor


carro_1 = Carro()

carro_2 = Carro()

carro_3 = Carro()

motocicleta_1 = Motocicleta()


print(f'Exemplo de como o carro nao tinha cor antes do uso do metodo {carro_3.cor}')

altera_cor(carro_1,'vermelho')

altera_cor(carro_2,'azul')

altera_cor(carro_3,'batata')

altera_cor(motocicleta_1,'batata')

print(f'Exemplo, de como o objeto teve sua cor alterada {carro_1.cor}')

print(f'Exemplo de como o metodo e utilizavel para qualquer objeto {motocicleta_1.cor}')

