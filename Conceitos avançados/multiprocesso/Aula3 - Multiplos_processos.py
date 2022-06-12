import time
import multiprocessing
import concurrent.futures

def faz_algo(segundos) -> None:
    print(f'Dormindo {segundos}')
    time.sleep(segundos)
    return f'Finalizando processo de {segundos} ... '


def main ():    
    # Modulo velho
    # processos = []
    # for _ in range(10):
    #     p = multiprocessing.Process(target=faz_algo,args = [2.5])
    #     p.start()
    #     processos.append(p)
    # for processo in processos:
    #     processo.join()
        # Apesar do meu computador nao ter 10 cores existe mecanica em que se procura
        # Por cores que estao inativos
        # Aqui basicamente, estamso iniciando multiplos threads ao mesmo tempo

    # Novo modulo
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # ProcessPoolExecutor e aquele que esta escolhendo qual core vai rodar
        # Qual funcao
        # Ele e um context manager que basicamente faz o processo.start ou seja, inicia ele pra mim
        # E depois ele o fecha. Eliminando codigo desnecessario
        # f1 = executor.submit(faz_algo,1)
        # f2 = executor.submit(faz_algo,1)
        # Criando objeto futuro igual a multithreading
        # f1.result()
        # f2.result()
        # Pegando resultados desse objeto
        segundos = [5,4,3,2,1]
        # future = [executor.submit(faz_algo,seg) for seg in segundos]
        # for f in concurrent.futures.as_completed(future):
        #     # Aqui estamos avaliando caso a funcao do thread foi terminada
        #     print(f.result())
        resultados = executor.map(faz_algo,segundos)
        for resultado in resultados:
            print(resultado)


if __name__ == '__main__':
    comeco = time.perf_counter()
    main()
    final = time.perf_counter()
    print(f'O programa demorou {final-comeco}')