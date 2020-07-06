import json
from pathlib import Path
from manejador_prov import ManejadorProvincias
from provincia import Provincia

class ObjectEncoder(object):
    __pathArchivo=None
    def __init__(self, pathArchivo):
        self.__pathArchivo=pathArchivo
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='ManejadorProvincias':
                provincias=d['provincias']
                manejador=class_()
                for i in range(len(provincias)):
                    dProvincia=provincias[i]
                    class_name=dProvincia.pop('__class__')
                    class_=eval(class_name)
                    atributos=dProvincia['__atributos__']
                    prov=class_(**atributos)
                    manejador.agregarProv(prov)
            return manejador
    def guardar(self, diccionario):
        with Path(self.__pathArchivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()
    def leer(self):
        with Path(self.__pathArchivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario