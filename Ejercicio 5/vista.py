import tkinter as tk
from lista_pacientes import ListaPacientes
from actualizar_pacientes import ActualizarPaciente
from paciente import Paciente

class VistaPacientes(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Pacientes")
        self.list = ListaPacientes(self, height=15)
        self.form = ActualizarPaciente(self)
        self.btn_new = tk.Button(self, text="Agregar Paciente")
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)
    def setControlador(self, ctrl):
        self.btn_new.config(command=ctrl.crearPaciente)
        self.list.bind_doble_click(ctrl.seleccionarPaciente)
        self.form.bind_save(ctrl.modificarPaciente)
        self.form.bind_delete(ctrl.borrarPaciente)
        self.form.bind_imc(ctrl.mostrarIMCPaciente)
    def agregarPaciente(self, paciente):
        self.list.insertar(paciente)
    def modificarPaciente(self, paciente, index):
        self.list.modificar(paciente, index)
    def borrarPaciente(self, index):
        self.form.limpiar()
        self.list.borrar(index)
    def obtenerDetalles(self):
        return self.form.crearPacienteDesdeFormulario()
    def verPacienteEnForm(self, paciente):
        self.form.mostrarEstadoPacienteEnFormulario(paciente)
    def verIMC(self, imc):
        
        if imc < 18.5:
            comp = "Peso inferior al normal"
        elif imc < 25:
            comp = "Peso normal"
        elif imc < 30:
            comp = "Peso superior al normal"
        else:
            comp = "Obesidad"
        
        aux = tk.Toplevel()
        aux.title("IMC")
        marco = tk.Frame(aux)
        marco.pack(side=tk.TOP, padx=10, pady=15)
        tk.Label(marco, text="IMC").grid(row=0, column=0)
        tk.Label(marco, text="Composicion corporal").grid(row=1, column=0)
        tk.Label(marco, text=str(imc), width=20, borderwidth=1, relief="solid").grid(row=0, column=1)
        tk.Label(marco, text=comp, width=20, borderwidth=1, relief="solid").grid(row=1, column=1)
        tk.Button(aux, text="Volver", command=aux.destroy).pack(side=tk.BOTTOM, padx=5, pady=5)
