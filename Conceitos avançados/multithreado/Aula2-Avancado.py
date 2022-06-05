import time
import threading 


comeco = time.perf_counter()

def faz_algo(segundos) -> None:
    print(f'Eu to dormindo por {segundos}')
    time.sleep(segundos)
    print('Eu terminei de dormir')

#t1 = threading.Thread(target = faz_algo)
# Aqui voce nao quer passar a execucao da funcao, ou seja, evite os parenteses depois da call
# Porque voce vai obrigar o metodo a ser rodado na thread/linha principal.


#Criar 10 threads
threads = []
for _ in range(0,10):
    t = threading.Thread(target = faz_algo,args = [1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


final = time.perf_counter()

print(f'Terminei de rodar {final - comeco} segundos ')
# Esse metodo se utilizando da biblioteca threading e o velho
# Atualmente, existe um metodo mais manual. Que nos da a oportunidade, de traduzir facilmente
# Um programa multithreader com um programa multiprocesser

