# --- O que e? --- #
# Um decorator, seria uma funcao capaz de modificar. O comportamento de outra funcao
# Sem alterar, o codigo da funcao que esta tendo o seu comportamento alterado


def funcao_fora(msg):
    messagem = msg
    # Variavel livre - Seria basicamente, uma variavel que tambem e utilizavel pela funcao_dentro()
    # Muito semelhante, ao  conceito de variavel de classe
    def funcao_dentro():
        print(msg)
    return funcao_dentro


# --- Closure --- #
minha_funcao = funcao_fora('Batata')
minha_funcao2 = funcao_fora('Jovim')
# Eu guardei a memoria de execucao da minha funcao de fora. Com essa variavel
# Agora eu ainda posso chamar a minha variavel livre conhecida como mensagem. Porque ela ainda esta na memoria
# Quando eu executar a funcao_dentro atraves de outra chamada 'usar' os parenteses
# O nome dado a isso e Closure. Quer seria a basicamente, uma funcao interna capaz de acessar as variaveis da funcao externa
# Exemplo de Closure
# minha_funcao()
# minha_funcao2()


# --- Decorator -- #
# Basicamente uma funcao que recebe outra funcao como argumento
# E adiciona algum tipo de funcionalidade sem alterar o codigo recebida como argumento

# Exemplo funcao decorator
def funcao_decorator(funcao_original):
    def funcao_encapsulada(*args,**kwargs):
        # Seria a funcao retornada, com os acrescimos da funcao decorator
        # Vale lembrar que os argumentos especiais, sao necessarios para possibilitar com que o user insira oq ele queira
        print('O decorator acrescentou uma mecanica, que seria essa propria mecancia acrescentada')
        return funcao_original(*args,**kwargs)
    return funcao_encapsulada

# Modo trivial
# def visu(msg):
#     print(f'A funcao visu rodo a mensagem {msg}')
# visu_decorado = funcao_decorator(visu)
# visu_decorado()
# Todo esse codigo aqui e igual ao codigo abaixo
#Modo estilo
@funcao_decorator
def visu(msg,nome):
    print(f'A funcao visu rodo a mensagem {msg}, {nome}')
visu('Hello','Joselito')
