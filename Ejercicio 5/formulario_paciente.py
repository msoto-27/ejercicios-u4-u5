import tkinter as tk
from tkinter import messagebox
from paciente import Paciente

class FormularioPaciente(tk.LabelFrame):
    fields = ("Apellido", "Nombre", "Teléfono", "Altura", "Peso")
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Paciente", padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()
    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry
    def mostrarEstadoPacienteEnFormulario(self, paciente):
        values = (paciente.getApellido(), paciente.getNombre(),
                  paciente.getTelefono(), paciente.getAltura(), paciente.getPeso())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)
    def crearPacienteDesdeFormulario(self):
        values = [e.get() for e in self.entries]
        paciente=None
        if '' in values:
            messagebox.showerror("Error de Validación", "Todos los campos son obligatorios")
        else:
            try:
                paciente = Paciente(values[0], values[1], values[2], float(values[3]), float(values[4]))
            except ValueError as e:
                mensaje = str(e)
                if "could not convert string to float" in str(e):
                    mensaje = "Formato de peso y/o altura no validos"
                messagebox.showerror("Error de Validación", mensaje, parent=self)
        return paciente
    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)
            
