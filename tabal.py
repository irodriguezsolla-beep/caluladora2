import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QComboBox,
    QWidget, QStackedLayout, QGridLayout, QLabel, QRadioButton,
    QHBoxLayout, QGroupBox
)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Principal")

        caixaV = QVBoxLayout()

        self.cmbTipo = QComboBox()
        self.cmbTipo.addItem("Alumno")
        self.cmbTipo.addItems(("Profesores", "Pas"))
        self.cmbTipo.setCurrentIndex(-1)
        self.cmbTipo.currentIndexChanged.connect(self.on_cmbTipo_setCurrentChanged)

        caixaV.addWidget(self.cmbTipo)

        self.tarxetas = QStackedLayout()

        # Panel Alumno
        panelAlumno = QWidget()
        maiaAlumno = QGridLayout()

        lblCiclo = QLabel("Ciclo")
        self.cmdCiclo = QComboBox()
        ciclos = ("DAM", "ASIR", "SMR", "IEA", "ADF")
        self.cmdCiclo.addItems(ciclos)
        self.cmdCiclo.setCurrentIndex(-1)

        self.rbtPrimeiro = QRadioButton("Primeiro")
        self.rbtSegundo = QRadioButton("Segundo")

        caixaRadio = QHBoxLayout()
        caixaRadio.addWidget(self.rbtPrimeiro)
        caixaRadio.addWidget(self.rbtSegundo)

        self.cmbAnoMatricula = QComboBox()
        cursosMatricula = ("25/26", "26/27", "27/28")
        self.cmbAnoMatricula.addItems(cursosMatricula)

        lblNomeNai = QLabel("Nome Nai")
        self.txtNomeNai = QtWidgets.QLineEdit()
        lblNomePai = QLabel("Nome Pai")
        self.txtNomePai = QtWidgets.QLineEdit()

        maiaAlumno.addWidget(lblCiclo, 0, 0)
        maiaAlumno.addWidget(self.cmdCiclo, 0, 1)
        maiaAlumno.addLayout(caixaRadio, 1, 0, 1, 2)
        maiaAlumno.addWidget(QLabel("Ano Matrícula"), 2, 0)
        maiaAlumno.addWidget(self.cmbAnoMatricula, 2, 1)
        maiaAlumno.addWidget(lblNomeNai, 3, 0)
        maiaAlumno.addWidget(self.txtNomeNai, 3, 1)
        maiaAlumno.addWidget(lblNomePai, 4, 0)
        maiaAlumno.addWidget(self.txtNomePai, 4, 1)

        panelAlumno.setLayout(maiaAlumno)

        # Paneles Profesores
        panelProfesores = QWidget()
        maiaProfesor = QVBoxLayout()

        # RadioButton Titor
        self.rbtTitor = QRadioButton("É titor?")
        maiaProfesor.addWidget(self.rbtTitor)

        # Selección de Ciclo
        caixaCicloProf = QHBoxLayout()
        lblCicloProf = QLabel("Ciclo:")
        self.cmbCicloProf = QComboBox()
        self.cmbCicloProf.addItems(ciclos)
        self.cmbCicloProf.setCurrentIndex(-1)
        caixaCicloProf.addWidget(lblCicloProf)
        caixaCicloProf.addWidget(self.cmbCicloProf)
        maiaProfesor.addLayout(caixaCicloProf)

        # Anos (Primeiro / Segundo)
        grupoAnos = QGroupBox("Curso")
        caixaAnos = QHBoxLayout()
        self.rbtPrimeiroAno = QRadioButton("1º Ano")
        self.rbtSegundoAno = QRadioButton("2º Ano")
        caixaAnos.addWidget(self.rbtPrimeiroAno)
        caixaAnos.addWidget(self.rbtSegundoAno)
        grupoAnos.setLayout(caixaAnos)
        maiaProfesor.addWidget(grupoAnos)

        # Nivel do Ciclo
        grupoNivel = QGroupBox("Nivel do ciclo")
        caixaNivel = QHBoxLayout()
        self.rbtBasico = QRadioButton("Ciclo Básico")
        self.rbtMedio = QRadioButton("Ciclo Medio")
        self.rbtSuperior = QRadioButton("Ciclo Superior")
        caixaNivel.addWidget(self.rbtBasico)
        caixaNivel.addWidget(self.rbtMedio)
        caixaNivel.addWidget(self.rbtSuperior)
        grupoNivel.setLayout(caixaNivel)
        maiaProfesor.addWidget(grupoNivel)

        panelProfesores.setLayout(maiaProfesor)

        # PAS
        panelPAS = QWidget()
        maiaPAS = QVBoxLayout()
        Ocupaciones = ("Secretario", "Vedel")

        # Selección de PAS
        caixaOcupacionPAS = QHBoxLayout()
        lblOcupacion = QLabel("Ocupación: ")
        self.cmbOcupacion = QComboBox()
        self.cmbOcupacion.addItems(Ocupaciones)
        self.cmbOcupacion.setCurrentIndex(-1)
        caixaOcupacionPAS.addWidget(lblOcupacion)
        caixaOcupacionPAS.addWidget(self.cmbOcupacion)
        maiaPAS.addLayout(caixaOcupacionPAS)

        panelPAS.setLayout(maiaPAS)

        self.tarxetas.addWidget(panelAlumno)
        self.tarxetas.addWidget(panelProfesores)
        self.tarxetas.addWidget(panelPAS)

        caixaV.addLayout(self.tarxetas)

        container = QWidget()
        container.setLayout(caixaV)
        self.setCentralWidget(container)

    def on_cmbTipo_setCurrentChanged(self, index):
        if index >= 0:
            self.tarxetas.setCurrentIndex(index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    window.show()
    sys.exit(app.exec())