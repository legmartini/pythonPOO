from time import sleep


class SimOuNao(Exception):
    def __str__(self):
        return 'Digite somente "s" para SIM e "n" para NÃO.'


class Jogo(object):
    def __init__(self):
        self.__cartoes = ('''
        1   3   5   7   9   11  13  15
        17  19  21  23  25  27  29  31
        33  35  37  39  41  43  45  47
        49  51  53  55  57  59  61  63
        ''', '''
        2   3   6   7   10  11  14  15
        18  19  22  23  26  27  30  31
        34  35  38  39  42  43  46  47
        50  51  54  55  58  59  62  63
        ''', '''
        4   5   6   7   12  13  14  15
        20  21  22  23  28  29  30  31
        36  37  38  39  44  45  46  47
        52  53  54  55  60  61  62  63
        ''', '''
        8   9   10  11  12  13  14  15
        24  25  26  27  28  29  30  31
        40  41  42  43  44  45  46  47
        56  57  58  59  60  61  62  63
        ''', '''
        16  17  18  19  20  21  22  23
        24  25  26  27  28  29  30  31
        48  49  50  51  52  53  54  55
        56  57  58  59  60  61  62  63
        ''', '''
        32  33  34  35  36  37  38  39
        40  41  42  43  44  45  46  47
        48  49  50  51  52  53  54  55
        56  57  58  59  60  61  62  63
        ''')
        self.__card = 0
        self.__num = 0
        self.main()

    def apresentacao(self):
        print('Pense em um número entre 1 e 63.')
        sleep(5)
        print('Vou lhe mostrar diversos cartões e você deve me dizer')
        print('se o cartão contêm ou não o número que você pensou.')
        sleep(3)


    def recebeEntradaDoUsuario(self):
        while True:
            try:
                resp = input('\nEssa cartela contêm o número que você pensou? ').lower()

                if not resp.isalpha():
                    print('Digite apenas letras!!')
                elif resp.startswith('s'):
                    return True
                elif resp.startswith('n'):
                    return False
                else:
                    raise SimOuNao

            except SimOuNao:
                print(SimOuNao())

    def imprimeNumeroSecreto(self):
        print('\nDeixa eu adivinhar...')
        sleep(2)
        print(f'Você pensou no número...')
        sleep(2)
        print(f'{self.__num}')

    def main(self):
        self.apresentacao()

        for i in range(len(self.__cartoes)):
            self.__card = i
            self.mostraCartao()
            self.adicionaNumero(self.recebeEntradaDoUsuario())

        self.imprimeNumeroSecreto()

    def mostraCartao(self):
        print(self.__cartoes[self.__card])

    def adicionaNumero(self, contem):
        if contem:
            self.__num += int(self.__cartoes[self.__card].split()[0])


if __name__ == '__main__':
    x = Jogo()
