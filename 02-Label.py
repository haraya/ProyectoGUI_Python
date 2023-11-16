#importar los paquetes para los labels
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap
import sys

#clase de la aplicacion
class AppHolaMundo(QWidget):
    def __init__(self): #constructor
        super(AppHolaMundo, self).__init__() #super es para acceder a objeto de una clase padre
        self.emptywindow()
    def emptywindow(self):
        self.setGeometry(100,100,400,600)
        self.setWindowTitle("Holaaa")
        self.displayLabel()

    def displayLabel(self):
        texto = QLabel(self)
        texto.setText("Hola soy un label")
        texto.move(500,20)

        image = r"images/ideogram.jpeg"
        try:
            with open(image):
                labelImage = QLabel(self)
                pixmap = QPixmap(image)
                labelImage.setPixmap(pixmap)
                labelImage.move(100,0)
        except:
            print("La imagen no se encuentra")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppHolaMundo()
    window.show()
    sys.exit(app.exec())

