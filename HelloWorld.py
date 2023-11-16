#Importar los paquetes PyQt6 .QtWidgets QApplication, Qwidget
import sys
from PyQt6.QtWidgets import QApplication, QWidget

class VentanaVacia(QWidget):
    #Creamos un constructor
    def __init__(self):
        super (VentanaVacia, self).__init__()
        self.initializeUi()

    #Creamos un metodo inicializador GUI
    def initializeUi(self):
        #Definimos el tamaño de la ventana, primero 2 valores son donde aparece, 2 ancho y largo
        self.setGeometry(100,100,400,600)
        #Titulo de la ventana
        self.setWindowTitle("Hola desde una Ventana")

if  __name__== '__main__':
    app = QApplication(sys.argv) # variable donde se ejecutara la app
    window = VentanaVacia() #variable donde se almace la app
    window.show() # mostrar la app
    sys.exit(app.exec())# para cerrar la app