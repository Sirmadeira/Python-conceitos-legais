import concurrent.futures
import time

comeco = time.perf_counter()

def faz_algo(segundos:int) -> str:
    print(f'Eu to aquecendo o leite por {segundos}')
    time.sleep(segundos)
    if segundos < 1.5:
        return "Eu terminei de aquecer o leite no microondas"
    else:
        return "O leite ta muita quente"

with concurrent.futures.ThreadPoolExecutor() as executor:
    # f1 = executor.submit(faz_algo,2) 
    # f2 = executor.submit(faz_algo,1)   
    # Submit executa a funcao e retorno um objeto futuro
    # O objeto futuro, e como se fosse uma capsulo de argumentos e metodos interessantes
    # Ele ja pode me dar o tempo que demora para um thread ser executada
    # Quando ele comecar quando ele termina
    # Se ele ta rodando
    # Logo ele e bem util para evitar print statements
    # Ele tambem me da a opcao, de verificar o resultado da funcao
    # print(f1.result())
    # print(f2.result())
    # Me retorno, ql foi o resultado da minha funcao
    # Algo interessante, para manter o tracking do qual esta sendo retornado
    tempo = [5,4,3,2,1]
    resultados = executor.map(faz_algo,tempo)
    # E como se eu tivesse feito, executor.submit().result() 5 vezes
    # Semelhante a um loo
    # Um jeito de criar multiplos thread e printar eles na ordem de inicio
    # Basicamente qunado eles comecam
    for resultado in resultados:
        print(resultado)


final = time.perf_counter()

print(f'Terminei de rodar {final - comeco} segundos ')