class ManejadorPacientes(object):
    __pacientes = None
    
    def __init__(self):
        self.__pacientes = []
    def getListaPacientes(self):
        return self.__pacientes
    def agregarPaciente(self, paciente):
        self.__pacientes.append(paciente)
        return paciente
    def getPacientes(self):
        return self.__pacientes
    def actualizarPaciente(self, paciente, indice):
        self.__pacientes[indice] = paciente
        return paciente
    def borrarPaciente(self, paciente):
        self.__pacientes.remove(paciente)
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            pacientes=[paciente.toJSON() for paciente in self.__pacientes]
            )
        return d
    