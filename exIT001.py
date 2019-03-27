import struct
import re


def main():
    pessoas = carregaCadastro()
    print(pessoas)

    while True:
        cmd = recebeCmd()

        if cmd.startswith('n'):
            addCadastro(pessoas)
        elif cmd.startswith('p'):
            if len(pessoas) == 0:
                print('Não há nenhum cadastro.')
            else:
                pegaCadastro(pessoas)
        else:
            break

    salvaCadastro(pessoas)


def carregaCadastro():
    try:
        arq = open('pessoas.decode', 'rb')
    except IOError:
        return {}
    else:
        pessoas = {}

        try:
            for num_char_nome in arq:
                num_char_nome = num_char_nome.split(b'\n')[0]

                decode = '%is Q Q' % struct.unpack('I', num_char_nome)[0]

                data = arq.readline().split(b'\n')[0]
                info = struct.unpack(decode, data)

                pessoas[info[0].decode()] = {'R.G.': info[1], 'C.P.F.': info[2]}

        except:
            print('Há um erro de formatação no arquivo.')
            return {}
        else:
            return pessoas


def recebeCmd():
    while True:
        print('Adicionar novo cadastro [n].')
        print('Procurar informações [p].')
        print('Sair do programa [s].')
        cmd = input('O que deseja fazer? ')

        if not cmd.isalpha():
            print('Digite apenas letras.')
        elif cmd.startswith('n') or cmd.startswith('p') or cmd.startswith('s'):
            return cmd
        else:
            print('Comando Inválido.')


def addCadastro(pessoas):
    nome = str(input("Nome: "))
    pessoas[nome] = {}

    pegaRG(pessoas[nome])
    pegaCPF(pessoas[nome])


def pegaRG(pessoas):
    while True:
        rg = input('RG: ')

        if not re.match(r'\d{2}\.\d{3}\.\d{3}.\d{2}', rg):
            print('RG digitado de forma incorreta.')
        else:
            pessoas['RG'] = rg
            break


def pegaCPF(pessoas):
    while True:
        cpf = input('CPF: ')

        if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            print('CPF digitado de forma incorreta.')
        else:
            pessoas['CPF'] = cpf
            break


def pegaCadastro(pessoas):
    while True:
        nome = input('Digite o nome da pessoa: ')

        if nome in pessoas:
            formataCadastro(pessoas, nome)
            break
        else:
            print('Cadastro não encontrado. Tente Novamente.')


def formataCadastro(pessoas, nome):
    print(f'Nome: {nome}')
    imprimeRG(pessoas[nome]['RG'])
    imprimeCPF(pessoas[nome]['CPF'])
    print()


def imprimeRG(rg):
    print(f'RG: {rg}')


def imprimeCPF(cpf):
    print(f'RG: {cpf}')


def salvaCadastro(pessoas):
    with open('pessoas.decode', 'wb') as arq:
        for nome in pessoas:
            num_de_chars = len(nome)
            num_data = struct.pack('I', num_de_chars)
            arq.write(num_data)
            arq.write(b'\n')

            info_data = struct.pack('%is Q Q'%num_de_chars, nome.encode(), pessoas[nome]['RG'], pessoas[nome]['CPF'])

            arq.write(info_data)
            arq.write(b'\n')


if __name__ == '__main__':
    main()
