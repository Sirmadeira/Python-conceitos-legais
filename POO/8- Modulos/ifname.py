#******************************
# if__name__ = '__main__'':
#    pass
# *******************************
#Porque se utilizar disso?
# 1- Utilizado para simbolizar, que a modulo/pyfile tem que ser rodado diretamente (basicamente uma bandeira falando executa o codigo aqui)
# 2- Podemo fazer mecanicas, que impedem ele de executar o seus arquivo caso ele esteja sendo importado

# Essa mecanica so e possivel, porque o interpretador python da a variavel __name__
# Do modulo que esta rodando, o nome '__main__'.

# Que que e um modulo? Basicamente uma file py sendo importada

print(__name__)
# Esse dunder metodo __name__ me retorno a variavel string  '__main__', porque tecnicamente a variavel __name__ do modulo
# Que executa o codigo e __main__

def corre():
    print('correndo')


if __name__ == '__main__':
    # A linha de codigo acima basicamente, esa verificando se esse modulo/pyfile esta sendo executado
    # Diretamente ou indiretamente
    # No else, statement dele basicamente estariamos rodando o codigo indiretamente
    # Porque a variavel __name__ dele, nao e igual '__main__' que nem o print acima demonstra
    print('Rodando esse modulo diretamente')
    corre()
    # pass
    # Basicamente impediria eu de rodar esse codigo
else:
    print("Rodando esse cara indiretamente (sendo usado em outro modulo )")


