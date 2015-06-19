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
    def check_state(self):
#        sender = self.sender()
#        validator = sender.validator()
#        state = validator.validate(sender.text(), 0)[0]
#        if state == QtGui.QValidator.Acceptable:
        palette = QtGui.QPalette()
#        palette_label = QtGui.QPalette()
#        if ',' in self.entradaNumero.text():
        if str(self.entradaNumero.text()).find(".") != -1 or str(self.entradaNumero.text()).find(",") != -1:
            print 'rojo'
#        if self.entradaNumero.text().count(',') != 0:
            palette.setColor(self.entradaNumero.backgroundRole(),QtGui.QColor(255,0,0))
            self.entradaNumero.setPalette(palette)
            self.button_bajarVarias.setEnabled(False)
            self.button_subirVarias.setEnabled(False)
            #palette_label.setColor(QtGui.QPalette.Foreground,QtGui.QColor(255,0,0)
            self.labelError.setText("<font color='red'>Solo numeros enteros</font>")
#            self.labelError.setPalette(palette_label)
#            color = '#c4df9b'
#        if state == QtGui.QValidator.Intermediate:
#            color = '#fff79a'
#        else:
#            color = '#f6989d'
        elif '' == self.entradaNumero.text():
            print 'amarillo'
            palette.setColor(self.entradaNumero.backgroundRole(),QtGui.QColor(255,255,0))
            self.entradaNumero.setPalette(palette)
            self.button_subirVarias.setEnabled(False)
#            self.button_subirVarias.setDisabled(True)
            self.button_bajarVarias.setEnabled(False)
#            color = '#c4df9b'
            self.labelError.setText('')
        else:
            print 'verde'
            palette.setColor(self.entradaNumero.backgroundRole(),QtGui.QColor(0,255,0))
            self.entradaNumero.setPalette(palette)
            self.button_subirVarias.setEnabled(True)
#            self.button_subirVarias.setDisabled(False)
            self.button_bajarVarias.setEnabled(True)
#            color = '#fff79a'
#        sender.setStyleSheet ('entradaNumero { background-color: %s }' % color)
            self.labelError.setText('')



    def init_ui(self):
        self.label = QtGui.QLabel('cantidad de personas')
        self.labelError = QtGui.QLabel('')
        h_layout = QtGui.QHBoxLayout()
        h_layout.addWidget(self.label)
        h2_layout = QtGui.QHBoxLayout()
        h3_layout =QtGui.QHBoxLayout()
        y_layout = QtGui.QVBoxLayout()
        y_layout.addLayout(h_layout)
        y_layout.addLayout(h2_layout)
        y_layout.addLayout(h3_layout)

#La entrada del numero
        self.entradaNumero = QtGui.QLineEdit(self)

#Validacion para asegurarme que solo se pueda pasarle a entradaNumero solo numeros naturales
        soloNumerosNaturales = QtGui.QIntValidator(self)
#El valor minimo es 0.0, el maximo 99999.0 y no puede pasar decimales
        soloNumerosNaturales.setRange(0,999999)

        self.entradaNumero.setValidator(soloNumerosNaturales)

#Seteo el color de fondo del QLineEdit entradaNumero con amarillo, dado que el estado inicialmente estara vacio
        palette = QtGui.QPalette()
        palette.setColor(self.entradaNumero.backgroundRole(),QtGui.QColor(255,255,0))
        self.entradaNumero.setPalette(palette)


        #entradaNumero.textChanged[str].connect(self.onChanged)

        button_subir = QtGui.QPushButton('Subir Persona')
        button_bajar = QtGui.QPushButton('Bajar Persona')
        button_subir5 = QtGui.QPushButton('Subir 5 Personas')
        button_bajar5 = QtGui.QPushButton('Bajar 5 Personas')
        self.button_subirVarias = QtGui.QPushButton('Subir Varias Personas')
        self.button_bajarVarias = QtGui.QPushButton('Bajar Varias Personas')


#Seteo como descativados los botones de subir y bajar varias personas dado
#que en un principio en entradaNumero no habra nada
#En el momento que se escriba algo se habilitara por check_state
        self.button_subirVarias.setEnabled(False)
        self.button_bajarVarias.setEnabled(False)


        h_layout.addWidget(button_subir)
        h_layout.addWidget(button_bajar)
        h_layout.addWidget(button_subir5)
        h_layout.addWidget(button_bajar5)
        h2_layout.addWidget(self.entradaNumero)
        h2_layout.addWidget(self.button_subirVarias)
        h2_layout.addWidget(self.button_bajarVarias)
        h3_layout.addWidget(self.labelError)
#        self.labelError.move(1,1)
#        y_layout.addStretch()





        button_subir.clicked.connect(self.controlador.handler_subir_persona)
        button_bajar.clicked.connect(self.controlador.handler_bajar_persona)
        button_subir5.clicked.connect(self.controlador.handler_subir5_persona)
        button_bajar5.clicked.connect(self.controlador.handler_bajar5_persona)
        self.button_subirVarias.clicked.connect(self.controlador.handler_subirVarias_personas)
        self.button_bajarVarias.clicked.connect(self.controlador.handler_bajarVarias_personas)
        self.entradaNumero.textChanged.connect(self.check_state)
#        self.entradaNumero.textChanged.emit(self.entradaNumero.text())


        self.setLayout(y_layout)
        self.setWindowTitle('Proyecto del Auto')
        self.setGeometry(200,200,100,100)
        self.show()

app = QtGui.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())