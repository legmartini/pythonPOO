class Ponto(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def Imprime(self):
        print(f'X = {self.x} || Y = {self.y}')


class Ret(object):
    def __init__(self, ponto=Ponto(), alt=0, larg=0):
        self.alt = alt
        self.larg = larg
        self.verticePartida = ponto

    def Centro(self):
        x = self.verticePartida.x + self.larg / 2
        y = self.verticePartida.y + self.alt / 2

        return Ponto(x, y)


def main():
    verticePartida = Ponto()
    rect = Ret()

    while True:
        comando = Menu()

        if comando.startswith('M'):
            mudaValores(rect)
        elif comando.startswith('I'):
            rect.Centro().Imprime()
        else:
            break


def Menu():
    while True:
        comando = input('Mudar valores (M), Imprimir centro (I) ou Fechar (F) ? ').upper()

        if not comando.isalpha():
            print('Digite apenas letras!')
        else:
            if comando.startswith('M') or comando.startswith('I') or comando.startswith('F'):
                return comando
            else:
                print('Comando inválido, tente novamente: ')


def mudaValores(rect):
    rect.larg = float(input('Digite o valor da largura:\n'))
    rect.altura = float(input('Digite o valor da altura:\n'))
    rect.verticePartida.x = float(input('Digite o valor do x do vértice de partida:\n'))
    rect.verticePartida.y = float(input('Digite o valor do y do vértice de partida:\n'))


main()
