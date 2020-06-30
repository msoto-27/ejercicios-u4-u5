from math import gcd

class Fraccion(object):
    __numerador = 0
    __denominador = 0
    
    def __init__(self, numerador, denominador):
        self.__numerador = numerador
        self.__denominador = denominador
    def __str__(self):
        return str(self.__numerador) + '/' + str(self.__denominador)
    def simplificar(self):
        mcd = gcd(self.__numerador, self.__denominador)
        num = int(self.__numerador / mcd)
        den = int(self.__denominador / mcd)
        if den == 1:
            r = num
        else:
            r = Fraccion(num, den)
        return r
    def getNumerador(self):
        return self.__numerador
    def getDenominador(self):
        return self.__denominador
    def __add__(self, otro):
        if not isinstance(otro, Fraccion):
            otro = Fraccion(otro, 1)
        num = self.__numerador * otro.getDenominador() + self.__denominador * otro.getNumerador()
        den = self.__denominador * otro.getDenominador()
        return Fraccion(num, den).simplificar()
    def __sub__(self, otro):
        if not isinstance(otro, Fraccion):
            otro = Fraccion(otro, 1)
        num = self.__numerador * otro.getDenominador() - self.__denominador * otro.getNumerador()
        den = self.__denominador * otro.getDenominador()
        return Fraccion(num, den).simplificar()
    def __mul__(self, otro):
        if not isinstance(otro, Fraccion):
            otro = Fraccion(otro, 1)
        num = self.__numerador * otro.getNumerador()
        den = self.__denominador * otro.getDenominador()
        return Fraccion(num, den).simplificar()
    def __truediv__(self, otro):
        if not isinstance(otro, Fraccion):
            otro = Fraccion(otro, 1)
        num = self.__numerador * otro.getDenominador()
        den = self.__denominador * otro.getNumerador()
        return Fraccion(num, den).simplificar()
    
    def __radd__(self, otro):
        return self + otro
    def __rsub__(self, otro):
        return (self - otro) * -1
    def __rmul__(self, otro):
        return self * otro
    def __rtruediv__(self, otro):
        return Fraccion(self.__denominador, self.__numerador) * otro
    