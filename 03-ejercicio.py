#Importamos los QApplication, Qwidget, Qlabel, QFont para darle textura, QPixmap
from PyQt6.QtWidgets import QWidget, QLabel, QApplication
from PyQt6.QtGui import QPixmap, QFont
from PyQt6 import QtGui
import sys

class InterfazUsuario(QWidget):
    def __init__(self):
        super(InterfazUsuario, self).__init__()
        self.initializeUi()

    def initializeUi(self):
        self.setGeometry(100,100,1100,600)
        self.setWindowTitle("Perfil de Usuario")
        self.setWindowIcon(QtGui.QIcon("images/iconprofile.png"))
        #Funciones creadas por nosotros
        self.mostrar_imagen()
        self.mostrar_label()

    def mostrar_imagen(self):
        #ruta de las imagenes
        foto_perfil = r"images/profile.jpg"
        foto_fondo = r"images/fondo.jpg"

        try:
            with open(foto_fondo):
                label_fondo = QLabel(self)
                pixmap = QPixmap(foto_fondo)
                label_fondo.setPixmap(pixmap)
        except FileNotFoundError:
            print("No se encuentra la imagen")

        try:
            with open(foto_perfil):
                label_perfil = QLabel(self)
                pixmap = QPixmap(foto_perfil)
                label_perfil.setPixmap(pixmap)
        except FileNotFoundError:
            print("No se encuentra la imagen")


    def mostrar_label(self):
        usuario = QLabel(self)
        usuario.setText("Maria Ramona")
        usuario.move(725, 100)
        usuario.setFont(QFont("Arial",24))

        #biografia
        biografia = QLabel(self)
        biografia.setText("Biografia")
        biografia.move(650,150)
        biografia.setFont(QFont("Arial", 22))

        #Descripcion
        descripcion = QLabel(self)
        descripcion.setText("Soy análista de datos con 8 años de experiencia dando los mejores reportes")
        descripcion.move(650, 185)

        descripcion.setFont(QFont("Arial", 16))
        descripcion.setWordWrap(True)

        #Skills
        habilidades = QLabel(self)
        habilidades.setText("Habilidades")
        habilidades.move(650,300)
        habilidades.setFont(QFont("Arial", 22))

        #habilidades tecnicas
        habilidades_tecnicas = QLabel(self)
        habilidades_tecnicas.setText("Python | SQL | Power BI | Excel")
        habilidades_tecnicas.move(650, 330)
        habilidades_tecnicas.setFont(QFont("Arial", 16))

        # experiencia titulo
        habilidades = QLabel(self)
        habilidades.setText("Experiencia")
        habilidades.move(650, 400)
        habilidades.setFont(QFont("Arial", 22))

        # experiencia descripcion 1
        experiencia1 = QLabel(self)
        experiencia1.setText("Analista de Datos")
        experiencia1.move(650, 430)
        experiencia1.setFont(QFont("Arial", 16))
        #mes
        mes = QLabel(self)
        mes.setText("Marzo 2022 - Presente")
        mes.move(650, 460)
        mes.setFont(QFont("Arial", 14))

        # experiencia descripcion  2
        experiencia1 = QLabel(self)
        experiencia1.setText("Taquitos de tu corazón")
        experiencia1.move(650, 500)
        experiencia1.setFont(QFont("Arial", 16))
        # mes
        mes = QLabel(self)
        mes.setText("Marzo 2011 - Diciembre 2022")
        mes.move(650, 530)
        mes.setFont(QFont("Arial", 14))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InterfazUsuario()
    window.show()
    sys.exit(app.exec())

