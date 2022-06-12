##################

#====Multiprocessing=====#

# Multiprocessing = Seria o processo em que voce rodas duas atividades em paralelo, on bases de cpu diferentes

from multiprocessing import Process,cpu_count
import time


def contador(num):
    count = 0
    while count < num:
        count += 1
        #print(count)



def main():

    print(cpu_count())
    # Deveria me retornar um quao rachado o meu cpu foi
    # No entanto ele me retorna sempre 16
    
    a = Process(target = contador,args = (num:=25000000,  ))
    b = Process(target=contador,args = (num:=25000000,))
    c = Process(target=contador,args = (num:=25000000,))
    d = Process(target=contador,args = (num:=25000000,))
    # Cuidado nao crie muitos processos nao vamos necessariamente
    # Aumentar a velociddade de processamento do programa
    # Muito porque criar o processo e fecha-lo tammbem tem custo de processamento para cpu
    # Entao tenha cuidado com retornos diminutivos

    a.start()
    b.start()
    c.start()
    d.start()

    print("Processando..")
    
    a.join()
    b.join()
    c.join()
    d.join()


    print(f"Finalizado em {time.perf_counter():.2f} segundos")


if __name__ == '__main__':
    main()

