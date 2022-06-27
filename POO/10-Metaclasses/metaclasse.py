# --- O que e uma  metaclasse? -- #
# Nao e nada mais do que uma classe, que herda um type constructor
# Que nao seria nada mais do que uma classe que cria um objeto, que so objeto e uma classe. 
# O trabalho principal de uma metaclassse, semelhante ao type constructor
# E criar uma classe, com alguma caracteristica especifica

import time

class MinhaMetaClasse(type):
    # Voce ta vendo que a minha meta classe esta herdando um type constructor
    # O que destaca para as pessoas, que eu pretendo criar uma classe
    # Com essa classe
    tempo_base = time.perf_counter()

    def __new__(mcs,name,bases,namespace):
    # E um metodo dunder, que acontece quando eu crio minha classe
        print(mcs,name,bases,namespace)
        namespace['__class_carrega_tempo__'] = time.perf_counter() - MinhaMetaClasse.tempo_base
        # Seria uma variavel, que tem um nome. E me retorna, o tempo demorado para criar a minha classe
        # Basicamente um atributo da classe
        return super().__new__(mcs,name,bases,namespace)
        # Basicamente destacando que as classes criada por essa meta classe
        # Herdaram os meus parametros do meu dunder new.


class A(metaclass = MinhaMetaClasse):
    pass

class B(A):
    pass


def main():
    a = A()
    # Criando um objeto
    print (f'{type(a)}')
    # Isso daki vai dar o nome do que o meu objeto que seria a minha
    print(f'{type(A)}')
    # Isso daki vai me dar o que cria a minha classe
    # Que seria a minha metaclasse
    # Se nao fosse uma metaclasse me retornaria o type constructor, que seria o criador padrao do python
    # Mas nesse caso o que cria essa classe A e a minha meta classe
    print(f'{A.__class_carrega_tempo__}')
    print(f'{B.__class_carrega_tempo__}')
    # Aqui podemos ver que metaclasse sao herdaveis
    # Uma caracteristica que somente a minha metaclasse podia ter foi herdada para sua class filho
main()