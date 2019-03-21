class Pessoa(object):
    def __init__(self, n='', i=0, p=0, a=0):
        self.nome = n
        self.idade = i
        self.peso = p
        self.altura = a

    def Dados(self):
        self.nome = str(input('Nome: '))
        self.idade = int(input('Idade: '))
        self.peso = float(input('Peso: '))
        self.altura = float(input('Altura: '))

    def Envelhecer(self):
        if self.idade < 21:
            self.idade += 1
            self.altura += 0.05
            print(f'Altura: {"%.2f" %self.altura} | Idade: {self.idade}')
        if self.idade >= 21:
            self.idade += 1
            self.altura += 0
            print(f'Idade: {self.idade}')

    def Engordar(self):
        self.peso += 1
        print(f'Peso: {self.peso}')

    def Emagrecer(self):
        self.peso -= 1
        print(f'Peso: {self.peso}')

    def Imprime(self):
        print(f'Nome: {self.nome}')


pessoa = Pessoa()
pessoa.Dados()
pessoa.Imprime()
pessoa.Envelhecer()
pessoa.Envelhecer()
pessoa.Envelhecer()
