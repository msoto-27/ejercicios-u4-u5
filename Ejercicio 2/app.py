import requests
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

class Conversor():
    __ventana = None
    __pesos = None
    __dolares = None
    __venta = None
    
    def __init__(self):
        
        r = requests.get("https://www.dolarsi.com/api/api.php?type=dolar")
        x = r.json()
        i = 0
        while i < len(x) and x[i]["casa"]["nombre"] != "Oficial":
            i += 1
        if i < len(x):
            self.__venta = float(x[i]["casa"]["venta"].replace(',', '.'))
        
        
        
        self.__ventana = Tk()
        self.__ventana.geometry('300x100')
        self.__ventana.title('Conversor de moneda')
        
        mainframe = ttk.Frame(self.__ventana, padding="5 15 15 5")
        mainframe.grid(column=0, row=0, sticky=("nsew"))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        
        self.__pesos = StringVar()
        self.__pesos.trace('w', self.convertir)
        self.__dolares = StringVar()
        
        
        p_ent = ttk.Entry(mainframe, width=15, textvariable=self.__pesos)
        p_ent.grid(column=1, row=0)
        ttk.Label(mainframe, textvariable=self.__dolares).grid(column=1, row=1)
        ttk.Label(mainframe, text="pesos").grid(column=2, row=0)
        ttk.Label(mainframe, text="es equivalente a").grid(column=0, row=1)
        ttk.Label(mainframe, text="dolares").grid(column=2, row=1)
        ttk.Button(mainframe, text="Salir", command=self.__ventana.destroy).grid(column=2, row=2)
    
        self.__ventana.mainloop()
    
    def convertir(self, *args):
        if self.__pesos:
            try:
                pesos = float(self.__pesos.get())
            except ValueError:
                if self.__pesos.get() == '':
                    self.__dolares.set("0")
                else:
                    self.__dolares.set("ERROR")
            else:    
                self.__dolares.set(round(self.__venta * pesos, 2))
        
        
def main():
    aplicacion = Conversor()

if __name__ == '__main__':
    main()