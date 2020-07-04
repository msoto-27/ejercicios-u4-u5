import re

class Paciente(object):
    telefonoRegex = re.compile(r"\([0-9]{3}\)[0-9]{7}")
    __apellido = ''
    __nombre = ''
    __telefono = ''
    __altura = 0
    __peso = 0
    def __init__(self, apellido, nombre, telefono, altura, peso):
        if self.telefonoRegex.match(telefono):
            self.__apellido = apellido
            self.__nombre = nombre
            self.__telefono = telefono
            self.__altura = altura
            self.__peso = peso
        else:
            raise ValueError("Formato de telefono no valido")
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getTelefono(self):
        return self.__telefono
    def getAltura(self):
        return self.__altura
    def getPeso(self):
        return self.__peso
    def getIMC(self):
        return round(float(self.__peso) / ((float(self.__altura) / 100) ** 2), 2)
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                apellido=self.__apellido,
                nombre=self.__nombre,
                telefono=self.__telefono,
                altura=self.__altura,
                peso=self.__peso
                )
            )
        return d