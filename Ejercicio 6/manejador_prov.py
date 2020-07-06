class ManejadorProvincias(object):
    __provincias = []
    def __init__(self):
        self.__provincias = []
    def agregarProv(self, provincia):
        self.__provincias.append(provincia)
    def getProvs(self):
        return self.__provincias
    def getProv(self, ind):
        return self.__provincias[ind]
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            provincias=[p.toJSON() for p in self.__provincias]
            )
        return d