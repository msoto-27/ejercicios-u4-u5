import tkinter as tk
from tkinter import messagebox

from provincia import Provincia

class Vista(tk.Tk):
    __lista = None
    __form = None
    def __init__(self):
        super().__init__()
        self.title("Lista de Provincias")
        self.__lista = ListaProvincias(self, height=15)
        self.__form = FormularioCompleto(self)
        self.btn = tk.Button(self, text="Agregar Provincia")
        self.__lista.pack(side=tk.LEFT, padx=10, pady=10)
        self.__form.pack(padx=10, pady=10)
        self.btn.pack(side=tk.BOTTOM, pady=5)
    def setControlador(self, ctrl):
        self.btn.config(command=ctrl.crearProv)
        self.__lista.bind_doble_click(ctrl.seleccionarProv)
    def verProv(self, prov):
        self.__form.mostrarEnForm(prov)
    def agregarProv(self, prov):
        self.__lista.insertar(prov)
    
class ListaProvincias(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs) #(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    def insertar(self, prov):
        self.lb.insert(tk.END, prov.getNombre())
    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)
    
        
class FormularioProvincias(tk.LabelFrame):
    fields = ("Nombre", "Capital", "Cantidad de habitantes", "Cantidad de departamentos/partidos")
    def __init__(self, master):
        super().__init__(master, text="Provincia", padx=10, pady=10)
        self.pos = 0
        self.entries = list(map(self.crearCampo, self.fields))
        
    def crearCampo(self, field):
        label = tk.Label(self, text=field)
        entry = tk.Entry(self, width=25)
        label.grid(row=self.pos, column=0, pady=5)
        entry.grid(row=self.pos, column=1, pady=5)
        self.pos += 1
        return entry
    def mostrarEnForm(self, prov):
        datos = (prov.getNombre(), prov.getCapital(), prov.getHab(), prov.getDept(), prov.getTemp(), prov.getST(), prov.getHumedad())
        for entry, dato in zip(self.entries, datos):
            entry.delete(0, tk.END)
            entry.insert(0, dato)
    def crearProv(self):
        values = [e.get() for e in self.entries]
        provincia = None
        if '' in values:
            messagebox.showerror("Error de Validación", "Todos los campos son obligatorios")
        else:
            try:
                provincia = Provincia(values[0], values[1], int(values[2]), int(values[3]))
            except ValueError:
                messagebox.showerror("Error de Validación", "Cantidad de habitantes y/o departamentos invalida", parent=self)
            except ConnectionError:
                messagebox.showerror(title="Error de Conexion", message="No ha sido posible obtener los datos meteorologicos de la provincia. Revise su conexion a internet y verifique que el nombre de la provincia esté bien escrito.")
        return provincia
            

class FormularioCompleto(FormularioProvincias):
    extra_fields = ("Temperatura", "Sensación térmica", "Humedad")
    def __init__(self, master):
        super().__init__(master)
        self.entries += list(map(self.crearCampo, self.extra_fields))

class NuevaProvincia(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.__provincia = None
        self.__form = FormularioProvincias(self)
        self.btn = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.__form.pack(padx=10, pady=10)
        self.btn.pack(pady=10)
    def confirmar(self):
        self.__provincia = self.__form.crearProv()
        if self.__provincia:
            self.destroy()
    def mostrar(self):
        self.grab_set()
        self.wait_window()
        return self.__provincia