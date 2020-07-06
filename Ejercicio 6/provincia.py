import requests

class Provincia(object):
    __nombre = ''
    __capital = ''
    __hab = 0
    __dept = 0
    __temp = 0.0
    __st = 0
    __humedad = 0
    __apikey = "7db9a7a8f1d7f34516878491ea82a334"
    def __init__(self, nombre, capital, hab, dept):
        self.__nombre = nombre
        self.__capital = capital
        self.__hab = hab
        self.__dept = dept
        url = "https://api.openweathermap.org/data/2.5/weather?q=" + self.__nombre.replace(' ', '%20') + "&units=metric&appid=" + self.__apikey
        try:
            r = requests.get(url)
            aux = r.json()
            self.__temp = aux["main"]["temp"]
            self.__st = aux["main"]["feels_like"]
            self.__humedad = aux["main"]["humidity"]
        except:
            raise ConnectionError
        
    def getNombre(self):
        return self.__nombre
    def getCapital(self):
        return self.__capital
    def getHab(self):
        return self.__hab
    def getDept(self):
        return self.__dept
    def getTemp(self):
        return self.__temp
    def getST(self):
        return self.__st
    def getHumedad(self):
        return self.__humedad
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                nombre=self.__nombre,
                capital=self.__capital,
                hab=self.__hab,
                dept=self.__dept
                )
            )
        return d
