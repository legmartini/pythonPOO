class ObjGrafico(object):
    def __init__(self, cor_interna, preenchida, cor_contorno):
        self.cor_interna = cor_interna
        self.preenchida = preenchida
        self.cor_contorno = cor_contorno


class Retangulo(ObjGrafico):
    def __init__(self, cor_interna='', preenchida='', cor_contorno='', base=0, altura=0, area=0, perimetro=0):
        super().__init__(cor_interna, preenchida, cor_contorno)
        self.base = base
        self.altura = altura
        self.area = area
        self.perimetro = perimetro

    def Area(self):
        self.base = float(input('Base: '))
        self.altura = float(input('Altura: '))
        self.area = self.base * self.altura
        print(f'Área: {self.area}')

    def Perimetro(self):
        self.perimetro = (self.base + self.altura) * 2
        print(f'Perímetro: {self.perimetro}')

    def Definicao(self):
        self.cor_interna = str(input('Interna: '))
        self.preenchida = str(input('Preenchida: '))
        self.cor_contorno = str(input('Contorno: '))
        print(f'Cor Interna: {self.cor_interna}')
        print(f'Preenchida: {self.preenchida}')
        print(f'Cor do Contorno: {self.cor_contorno}')


class Triangulo(ObjGrafico):
    def __init__(self, cor_interna='', preenchida='', cor_contorno='', base=0, altura=0, area=0):
        super().__init__(cor_interna, preenchida, cor_contorno)
        self.base = base
        self.altura = altura
        self.area = area

    def Area(self):
        self.base = float(input('Base: '))
        self.altura = float(input('Altura: '))
        self.area = self.base * self.altura
        print(f'Área: {self.area}')

    def Definicao(self):
        self.cor_interna = str(input('Interna: '))
        self.preenchida = str(input('Preenchida: '))
        self.cor_contorno = str(input('Contorno: '))
        print(f'Cor Interna: {self.cor_interna}')
        print(f'Preenchida: {self.preenchida}')
        print(f'Cor do Contorno: {self.cor_contorno}')


class Circulo(ObjGrafico):
    def __init__(self, cor_interna='', preenchida='', cor_contorno='', raio=0, area=0, perimetro=0):
        super().__init__(cor_interna, preenchida, cor_contorno)
        self.raio = raio
        self.area = area
        self.perimetro = perimetro

    def Area(self):
        self.raio = float(input('Raio: '))
        self.area = self.raio * 3.14159
        print(f'Área: {self.area}')

    def Perimetro(self):
        self.perimetro = self.raio * (3.14159 * 2)
        print(f'Perímetro: {self.perimetro}')

    def Definicao(self):
        self.cor_interna = str(input('Interna: '))
        self.preenchida = str(input('Preenchida: '))
        self.cor_contorno = str(input('Contorno: '))
        print(f'Cor Interna: {self.cor_interna}')
        print(f'Preenchida: {self.preenchida}')
        print(f'Cor do Contorno: {self.cor_contorno}')


'''
objRet = Retangulo()
objRet.Area()
objRet.Perimetro()
objRet.Definicao()
objTri = Triangulo()
objTri.Area()
objTri.Definicao()
objCir = Circulo()
objCir.Area()
objCir.Perimetro()
objCir.Definicao()
'''

