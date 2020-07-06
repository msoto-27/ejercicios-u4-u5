from vista import NuevaProvincia

class Controlador(object):
    __vista = None
    __objenc = None
    __modelo = None
    __seleccion = None
    __objenc = None
    def __init__(self, vista, objenc):
        self.__vista = vista
        self.__objenc = objenc
        d = self.__objenc.leer()
        self.__modelo = self.__objenc.decodificarDiccionario(d)
        self.__seleccion = -1
    def crearProv(self):
        nueva_prov = NuevaProvincia(self.__vista).mostrar()
        if nueva_prov:
            self.__modelo.agregarProv(nueva_prov)
            self.__vista.agregarProv(nueva_prov)
    def seleccionarProv(self, ind):
        self.__seleccion = ind
        prov = self.__modelo.getProv(self.__seleccion)
        self.__vista.verProv(prov)
    def iniciar(self):
        for p in self.__modelo.getProvs():
            self.__vista.agregarProv(p)
        self.__vista.mainloop()
    def guardar(self):
        self.__objenc.guardar(self.__modelo.toJSON())
            