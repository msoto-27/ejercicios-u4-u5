import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

class App():
    __ventana = None
    __altura = None
    __peso = None
    __imc = None
    def __init__(self):
        
        #Ventana
        self.__ventana = Tk()
        self.__ventana.geometry('400x185')
        self.__ventana.title('Calculadora de IMC')
        
        #Variables de texto
        self.__altura = StringVar()
        self.__peso = StringVar()
        self.__imc = StringVar()
        self.__clasif = StringVar()
        
        #Frame principal
        mainframe = ttk.Frame(self.__ventana)
        mainframe.grid(column=0, row=0, sticky=("nsew"))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
            
        #Entries
        self.altura_entry = ttk.Entry(mainframe, width=30, textvariable=self.__altura)
        self.peso_entry = ttk.Entry(mainframe, width=30, textvariable=self.__peso)
        ttk.Label(mainframe, textvariable=self.__imc)
        
        #Posicionamiento
        titulo = tk.Label(mainframe, text="Calculadora de IMC").grid(column=2, row=0)
        ttk.Label(mainframe, text="Altura:").grid(column=0, row=1, padx=10, pady=10, sticky=N+S+E+W) #.pack(anchor=NW)#, side=LEFT)
        self.altura_entry.grid(column=1, row=1, columnspan=3)
        ttk.Label(mainframe, text="cm").grid(column=4, row=1)
        ttk.Label(mainframe, text="Peso:").grid(column=0, row=2, pady=10)
        self.peso_entry.grid(column=1, row=2, columnspan=3)
        ttk.Label(mainframe, text="kg").grid(column=4, row=2)
        
        ttk.Button(mainframe, text="Calcular", command=self.calcular).grid(column=1, row=3)
        ttk.Button(mainframe, text="Limpiar", command=self.limpiar).grid(column=3, row=3)
        
        #Frame resultado
        resultado = ttk.Frame(mainframe)
        resultado.grid(column=2, row=4)
        ttk.Label(resultado, text="Tu indice de masa corporal es").pack(side=TOP)
        ttk.Label(resultado, textvariable=self.__imc).pack(side=TOP)
        ttk.Label(resultado, textvariable=self.__clasif).pack(side=TOP)
        
        
        
        self.__ventana.mainloop()
        
    def calcular(self):
        try:
            imc = round(float(self.__peso.get()) / ((float(self.__altura.get()) / 100) ** 2), 2)
            self.__imc.set(str(imc))
            if imc < 18.5:
                cla = "Peso inferior al normal"
            elif imc < 25:
                cla = "Peso normal"
            elif imc < 30:
                cla = "Peso superior al normal"
            else:
                cla = "Obesidad"
            self.__clasif.set(cla)
        
        except ValueError:
            messagebox.showerror(title="Error de tipo", message="Debe ingresar valores numericos")
    def limpiar(self):
        self.__altura.set('')
        self.__peso.set('')
        
if __name__ == '__main__':
    aplicacion = App()