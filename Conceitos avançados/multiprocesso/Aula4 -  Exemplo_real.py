import time
import concurrent.futures
import os
from PIL import Image,ImageFilter

img_nome = os.listdir(r'C:\Users\FranciscoFroes\Documents\GitHub\Python-conceitos-legais\Conceitos avançados\multiprocesso\imagens')

path = "C:/Users/FranciscoFroes/Documents/GitHub/Python-conceitos-legais/Conceitos avançados/multiprocesso/imagens/"

tamanho_da_imagem = (1200,1200)

def processador_imagens(img_nome):

    t1 = time.perf_counter()

    for i in img_nome:
        img = Image.open(path + i)
        img = img.filter(ImageFilter.GaussianBlur(15))
        img.thumbnail(tamanho_da_imagem)
        img.save(path + i)
        print(f'{i} foi processada')


    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(processador_imagens,img_nome)

    t2 = time.perf_counter()

    print(f'Acabou de processar as imagens em {t2-t1}')

if __name__ == '__main__':
    processador_imagens(img_nome)
