class Banco(object):
    __total = 10000
    txreserva = 0.1
    __reserva = __total * txreserva

    def emprestimo(valor):
        Banco.__total -= valor
        if Banco.__total >= Banco.txreserva:
            Permitir = True
        else:
            Permitir = False

        Banco.__total += valor

        return Permitir

    def alteratotal(valor):
        Banco.__total += valor


class Conta(object):
    def __init__(self, saldo, ident="", senha=""):
        self.__saldo = saldo
        self.__ident = ident
        self.__senha = senha

    def identif(self):
        self.__ident = str(input('ID: '))
        self.__senha = str(input('SENHA: '))

    def deposito(self, senha, valor):
        if senha == self.__senha:
            self.__saldo += valor
            Banco.alteratotal(valor)

    def saque(self, senha, valor):
        if senha == self.__senha:
            self.__saldo = valor
            Banco.alteratotal(-valor)

    def permemprestimo(self, valor):
        return Banco.emprestimo(valor)

    def saldo(self):
        print(self.__saldo)

