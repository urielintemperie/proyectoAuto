# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
sys.path.append('../Controladores')
from main_controller import *

class MainWindow (QtGui.QWidget):

    def __init__(self):
        super(MainWindow , self).__init__()
        self.controlador = MainControlador(self)
        self.init_ui()

#    def check_state(self, *args, **kwargs):
#        sender = self.sender()
#        validator = sender.validator()
#        state = validator.validate(sender.text(), 0)[0]
#        if state == QtGui.QValidator.Acceptable:
#            color = '#c4df9b'
#        if state == QtGui.QValidator.Intermediate:
#            color = '#fff79a'
#        else:
#            color = '#f6989d'
#        sender.setStyleSheet ('entradaNumero { background-color: %s }' % color)



    def init_ui(self):
        self.label = QtGui.QLabel('cantidad de personas')
        h_layout = QtGui.QHBoxLayout()
        h_layout.addWidget(self.label)

#La entrada del numero
        self.entradaNumero = QtGui.QLineEdit(self)

#Validacion para asegurarme que solo se pueda pasarle a entradaNumero solo numeros naturales
        soloNumerosNaturales = QtGui.QIntValidator(self)
#El valor minimo es 0.0, el maximo 99999.0 y no puede pasar decimales
        soloNumerosNaturales.setRange(0,999999)

        self.entradaNumero.setValidator(soloNumerosNaturales)

        #entradaNumero.textChanged[str].connect(self.onChanged)

        button_subir = QtGui.QPushButton('Subir Persona')
        button_bajar = QtGui.QPushButton('Bajar Persona')
        button_subir5 = QtGui.QPushButton('Subir 5 Personas')
        button_bajar5 = QtGui.QPushButton('Bajar 5 Personas')
#        self.entradaNumero.textChanged.connect(self.check_state)
#        self.entradaNumero.textChanged.emit(self.entradaNumero.text())
        button_subirVarias = QtGui.QPushButton('Subir Varias Personas')
        button_bajarVarias = QtGui.QPushButton('Bajar Varias Personas')

        h_layout.addWidget(button_subir)
        h_layout.addWidget(button_bajar)
        h_layout.addWidget(button_subir5)
        h_layout.addWidget(button_bajar5)
        h_layout.addWidget(self.entradaNumero)
        h_layout.addWidget(button_subirVarias)
        h_layout.addWidget(button_bajarVarias)





        button_subir.clicked.connect(self.controlador.handler_subir_persona)
        button_bajar.clicked.connect(self.controlador.handler_bajar_persona)
        button_subir5.clicked.connect(self.controlador.handler_subir5_persona)
        button_bajar5.clicked.connect(self.controlador.handler_bajar5_persona)
        button_subirVarias.clicked.connect(self.controlador.handler_subirVarias_personas)
        button_bajarVarias.clicked.connect(self.controlador.handler_bajarVarias_personas)


        self.setLayout(h_layout)
        self.setWindowTitle('Proyecto del Auto')
        self.setGeometry(200,200,200,200)
        self.show()

app = QtGui.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())