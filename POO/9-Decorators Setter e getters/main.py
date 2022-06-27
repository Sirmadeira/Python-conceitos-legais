 # Um property decorator nos ajuda a definir um metodo
 # E utiliza-lo como um atributo
 # Muito util, quando voce quer se utilizar de atributos que dependem, de variaveis recebidas pelo usuario


class Empregado:
    def __init__(self, primeiro:str, ultimo:str):
        self.primeiro = primeiro
        self.ultimo = ultimo    

    @property
    # Isso daki me obriga a se utilizar desse acao como se fosse uma caracteristica da classe
    # Ou melhor dito um atributo
    def email(self)->str:
        return f'{self.primeiro}{self.ultimo}@hotmail.com'

    @property
    # Seria o getter, possibilitar eu acessar variaveis de outros metodos
    def nome_completo(self)->str:
        return f'{self.primeiro} {self.ultimo}'


    @nome_completo.setter
    # Aqui eu vou estar alterando as outras variaveis, qunado eu me utilizo desse metodo
    # Por exemplo, as variaveis. Primeiro e ultimo, serao alteradas caso eu de call nesse metodo
    # Por isso o nome, setter pq ele define
    def nome_completo(self,nome)->str:
        primeiro,ultimo = nome.split(' ')
        self.primeiro = primeiro
        self.ultimo = ultimo

    @nome_completo.deleter
    # Aqui eu vou deletar o empregado, e o seus atributos
    # Por isso nome  deleter
    def nome_completo(self)->str:
        self.primeiro = None
        self.ultimo = None

    

emp_1 = Empregado('Joselito','Batata')

print(emp_1.email)
#print(emp_1.email())
# Caso eu tente rodar esse metodo como um metodo, eu vou ter erro pq ele e na realidade e tratado como um atributo

print(emp_1.nome_completo)
# Agora eu tenho a capacidade de alterar, os nomes passados. Pelo constructor no inicio da classe
# O q significa que quando eu redefinir, o nome completo do usuario tambem vou alterar o primeiro e ultimo nome dele
# Que estao sendo definido em outro metodo

emp_1.nome_completo = "Batatinha Macarrao"

print(emp_1.nome_completo)

del emp_1.nome_completo
#Exemplo, de como eu posso deletar o nome do empregado com um deleter

print(emp_1.primeiro)
