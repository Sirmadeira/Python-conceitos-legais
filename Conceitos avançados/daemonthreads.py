# Daemon threads - Um thread que basicamente, nao e  muito importante para o programa ser executada
# O seu programa, nao vai esperar o daemon thread finalizar a sua execucao para encerrar ele por completo
# Threads non daemon, normalmente nao podem ser finalizados , antes deles terminarem a suas acao acabar.
# Exemplo, de quando e utilizado: Em tarefas secundarias, colecao de lixo, esperando por input (contadores)


import threading
import time


# Funcao contador (exemplo de funcao que voce desejaria no background)
# Nao e super importante, mas e legalzinho de ter
# Para verificar quanto tempo o user demora pra responder

def contador() -> None:
    print()
    count = 0
    while True:
        time.sleep(1)
        count+=1
        print(f'O usuario nao respondeu por {count}')

# Criando thread
x = threading.Thread(target = contador,daemon = True)
# Para converter o thread em daemon, so acrescentar o parametro daemon = True

x.start()

#x.setDaemon(True)
# Outro jeito de garantir que Daemon

print(x.isDaemon())
# Verifica se o seu thread e daemon


resposto = input("Voce deseja sair?")