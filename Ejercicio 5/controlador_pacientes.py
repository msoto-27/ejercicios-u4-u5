from vista import VistaPacientes
from nuevo_paciente import NuevoPaciente
from manejador_pacientes import ManejadorPacientes
from encoder import ObjectEncoder


class ControladorPacientes(object):
    __enc = None
    __manejador = None
    def __init__(self, enc, vista):
        self.__enc = enc
        diccionario = enc.leerJSONArchivo()
        self.__manejador = enc.decodificarDiccionario(diccionario)
        self.vista = vista
        self.seleccion = -1
        self.pacientes = list(self.__manejador.getListaPacientes())
    def crearPaciente(self):
        nuevoPaciente = NuevoPaciente(self.vista).mostrar()
        if nuevoPaciente:
            paciente = self.__manejador.agregarPaciente(nuevoPaciente)
            self.pacientes.append(paciente)
            self.vista.agregarPaciente(paciente)
    def seleccionarPaciente(self, index):
        self.seleccion = index
        paciente = self.pacientes[index]
        self.vista.verPacienteEnForm(paciente)
    def modificarPaciente(self):
        if self.seleccion==-1:
            return
        detallesPaciente = self.vista.obtenerDetalles()
        paciente = self.__manejador.actualizarPaciente(detallesPaciente, self.seleccion)
        self.pacientes[self.seleccion] = paciente
        self.vista.modificarPaciente(paciente, self.seleccion)
        self.seleccion=-1
    def borrarPaciente(self):
        if self.seleccion==-1:
            return
        paciente = self.pacientes[self.seleccion]
        self.__manejador.borrarPaciente(paciente)
        self.pacientes.pop(self.seleccion)
        self.vista.borrarPaciente(self.seleccion)
        self.seleccion=-1
    def mostrarIMCPaciente(self):
        if self.seleccion==-1:
            return
        imc = self.pacientes[self.seleccion].getIMC()
        self.vista.verIMC(imc)
        
    def iniciar(self):
        for c in self.pacientes:
            self.vista.agregarPaciente(c)
        self.vista.mainloop()
    def salirGrabarDatos(self):
        self.__enc.guardarJSONArchivo(self.__manejador.toJSON())