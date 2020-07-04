from vista import VistaPacientes
from controlador_pacientes import ControladorPacientes
from encoder import ObjectEncoder
from paciente import Paciente
from manejador_pacientes import ManejadorPacientes

def main():
    con = ObjectEncoder("pacientes.json")
    manej = ManejadorPacientes()
    vista = VistaPacientes()
    ctrl = ControladorPacientes(con, vista)
    vista.setControlador(ctrl)
    ctrl.iniciar()
    ctrl.salirGrabarDatos()
    
if __name__ == '__main__':
    main()