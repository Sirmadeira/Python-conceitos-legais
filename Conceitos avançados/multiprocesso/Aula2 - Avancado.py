import time
import multiprocessing

def faz_algo() -> None:
    print(f'Dormindo 1')
    time.sleep(1)
    print(f'Finalizando ... ')

def main ():
    comeco = time.perf_counter()

    p1 = multiprocessing.Process(target=faz_algo)
# # Criando objeto processador mesmo coisa do que o thread
# p2 = multiprocessing.Process(target=faz_algo)

    p1.start()
    p1.join()


    final = time.perf_counter()
    print(f'O programa demorou {final-comeco}')


# p2.start()


if __name__ == '__main__':
    main()