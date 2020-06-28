import requests
import datetime
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

class Cotizacion():
    __frame = None
    __fecha_hora = None
    
    def __init__(self):
        
        ventana = Tk()
        ventana.geometry('350x250')
        ventana.title('Cotizaciones del dolar')
        
        self.__frame = ttk.Frame(ventana)
        self.__frame.grid(column=0, row=0, sticky=("nsew"))
        self.__frame.columnconfigure(0, weight=1)
        self.__frame.rowconfigure(0, weight=1)
        
        self.__fecha_hora = StringVar()
        fila = self.actualizar()
        
        if fila == None:
            ventana.destroy()
        
        ttk.Label(self.__frame, text="Nombre").grid(row=0, column=0, pady=10)
        ttk.Label(self.__frame, text="Compra").grid(row=0, column=1, pady=10)
        ttk.Label(self.__frame, text="Venta").grid(row=0, column=2, pady=10)
        
        ttk.Button(self.__frame, text="Actualizar", command=self.actualizar).grid(row=fila, column=0)
        ttk.Button(self.__frame, text="Salir", command=ventana.destroy).grid(row=fila, column=2)
        ttk.Label(self.__frame, text="Ultima actualizacion:").grid(row=fila+1, column=0)
        
        
        ttk.Label(self.__frame, textvariable=self.__fecha_hora).grid(row=fila+1, column=1)
        
        ventana.mainloop()
    
    def actualizar(self, *args):
        try:
            r = requests.get("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
        except:
            messagebox.showerror(title="Error de conexion", message="No ha sido posible obtener los valores actualizados. Revise su conexion a internet y vuelva a intentarlo.")
            i = None
        else:
            x = r.json()
        
            i = 1
            for d in x:
                if "Dolar" in d["casa"]["nombre"]:
                    ttk.Label(self.__frame, text=d["casa"]["nombre"]).grid(row=i, column=0)
                    ttk.Label(self.__frame, text=d["casa"]["compra"]).grid(row=i, column=1)
                    ttk.Label(self.__frame, text=d["casa"]["venta"]).grid(row=i, column=2)
                    i +=1
                self.__fecha_hora.set(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        
        return i
        
        
def main():
    aplicacion = Cotizacion()

if __name__ == '__main__':
    main()