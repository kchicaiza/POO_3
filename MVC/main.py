from modelo import*
from vista import*
from controlador import*

modelo = ListaTanques()
vista = VistaTanques()
controlador = ControladorTanques(modelo, vista)
controlador.ejecutar()

