import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QGridLayout,
    QPushButton, QWidget, QLabel, QSizePolicy  # <--- Importamos QSizePolicy
)
from PyQt6.QtGui import QPalette, QColor

class CaixaCor(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(paleta)

class Ventana(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora Isaac")
        self.setMinimumSize(200, 400)
        self.setMaximumSize(500, 400)

        # 1. Crear el grid layout
        grid = QGridLayout()

        # 2. Pantalla gris (Fila 0, Ocupa 1 fila y 5 columnas)
        self.pantalla = QLabel()

        grid.addWidget(pantalla, 0, 0, 1, 5)

        # 3. Fila 1
        grid.addWidget(QPushButton("⌫"), 1, 0)
        grid.addWidget(QPushButton("("), 1, 1)
        grid.addWidget(QPushButton(")"), 1, 2)
        grid.addWidget(QPushButton("mod"), 1, 3)
        grid.addWidget(QPushButton("π"), 1, 4)

        # 4. Fila 2
        grid.addWidget(QPushButton("7"), 2, 0)
        grid.addWidget(QPushButton("8"), 2, 1)
        grid.addWidget(QPushButton("9"), 2, 2)
        grid.addWidget(QPushButton("÷"), 2, 3)
        grid.addWidget(QPushButton("√"), 2, 4)

        # 5. Fila 3
        grid.addWidget(QPushButton("4"), 3, 0)
        grid.addWidget(QPushButton("5"), 3, 1)
        grid.addWidget(QPushButton("6"), 3, 2)
        grid.addWidget(QPushButton("×"), 3, 3)
        grid.addWidget(QPushButton("X²"), 3, 4)

        # 6. Fila 4
        grid.addWidget(QPushButton("1"), 4, 0)
        grid.addWidget(QPushButton("2"), 4, 1)
        grid.addWidget(QPushButton("3"), 4, 2)
        grid.addWidget(QPushButton("-"), 4, 3)

        # 7. Fila 5
        grid.addWidget(QPushButton("0"), 5, 0)
        grid.addWidget(QPushButton(","), 5, 1)
        grid.addWidget(QPushButton("%"), 5, 2)
        grid.addWidget(QPushButton("+"), 5, 3)

        # 8. Botón "=" único (Ocupa 2 filas verticalmente: de la fila 4 a la 5 en la columna 4)
        btn_igual = QPushButton("=")
        # ANOTACIÓN: Esta línea permite que el botón se expanda verticalmente para llenar todo el alto de las 2 filas
        btn_igual.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        grid.addWidget(btn_igual, 4, 4, 2, 1)

        # Asignar el contenedor central
        contenedor = QWidget()
        contenedor.setLayout(grid)
        self.setCentralWidget(contenedor)

        def numeropulsado(self):
            boton = self.sender()#saber boton que clicaste
            num = boton.text() #escriba

            if self.operador == "":
                self.num1 = self.num1 + num
                self.pantalla.setText(self.num1)
            else:
                self.num2 = self.num2 + num
                self.pantalla.setText(self.num2)
            print("Numero 1:" + self.num1)
            print("Numero 2:" + self.num2)


fwuv

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show()
    sys.exit(app.exec())