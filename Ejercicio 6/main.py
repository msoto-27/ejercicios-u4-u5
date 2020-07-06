from controlador import Controlador
from vista import Vista
from encoder import ObjectEncoder

def main():
    objenc = ObjectEncoder("datos.json")
    vista = Vista()
    ctrl = Controlador(vista, objenc)
    vista.setControlador(ctrl)
    ctrl.iniciar()
    ctrl.guardar()
    
    
if __name__=='__main__':
    main()