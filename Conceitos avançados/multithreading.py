# Thread = Thread e igual a um rio de execucao. Como se foose uma lista de instrucoes
        # E como se a gente rachasse o nosso programa em partes
        # E executasse, os processo do programa em simultaneidade(ao mesmo tempo) mas nao necessariamente em paralelo (dois threads no mesmo ponto e periodo
        # Em paraleloe chamado de multiprocessing
        # No multiprocessing nao podemos rodar em paralelo, devido ao GIL = Global interpreter lock
        # Que cria a condicao de q somente um fio pode ter controle do interpretador
        # Por isso cada um tem que ter seu devido turno.

# Os threads sao divididos em duas categorias.

# Preso ao cpu - Programa, passa muito tempo esperado eventos internos(dependentes do seu pc) no seu CPU, quando os programas sao muito ao associado ao CPU e melhor usar
# Multiprocessing

# Preso a IO = Programa, passa muito tempo esperando eventos de usuarios. (Inputs, web scraping) quando e assim se utilizar de multithreading
# Um bom exemplo, de multithreading: Seria num jogo de quiz
# Onde enquanto voce espera a resposta do seu usuario voce pode fazer um countodwn. Em um thread diferente
# Nesse caso, os thread estao rodando em simultaneidade, ja que um esta "travado" (esperando input) e o outro estava sendo executado mas nao e paralelo
# Um so e feito, qnd o outro "pausa"

from ast import arg
import threading
# Modulo necessario para verificar o fio que esta rodando o codigo
import time
from urllib.parse import ParseResultBytes

#print(threading.active_count())
# Retorna o numero de fios sendo executados
#print(threading.enumerate())
# Me da o nome, do thread que esta sendo executado


# Exemplo, de quando multithreading pode ser util
def comer():
    time.sleep(2)
    # Comer demorar 2 segundos
    print("Voce come o cafe da manha")

def beber():
    time.sleep(4)
    print("Voce bebe o cafe")

def estudar():
    time.sleep(8)
    print("Voce comeca a estudar")



tempo_de_inicio = time.time()

x = threading.Thread(target=comer,args=())
x.start()
y = threading.Thread(target=beber,args=())
y.start()
z = threading.Thread(target=estudar,args=())
z.start()


# comer()
# beber()
# estudar()
# Comentamos, isso daki nao queremos mais que o thread main seja o responsavel
# Por rodar as funcoes
# Se rodarmos isso no mesmo thread, demoramos 14 segundos
# Porque para comecarmos uma tarefa temos que terminar a outra
# No entanto, podemos fazer uma enquanto a gente espera  o outro


x.join()
y.join()
#Junta os threads criados ao main thread, e bom qnd a gente qr q uma tarefa seja executada, logo em seguida de um evento
# Ou quando q a gente paralelizar ela devido a um evento de outra

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter)
# Verifica qnt tempo,  a main thread demora para executar o codigo de criacao de funcoes e prints
