# -*- coding: utf-8 -*-
import sys
sys.path.append('../Modelo')
from auto import *


class MainControlador():

    def __init__(self, una_ventana):
        self.auto = Auto()
        self.ventana = una_ventana

    def handler_subir_persona(self):
        self.auto.subir_persona()
        self.actualizar_label()


    def handler_bajar_persona(self):
        self.auto.bajar_persona()
        self.actualizar_label()

    def handler_subir5_persona(self):
        contador = 0
        while contador<5:
            self.handler_subir_persona()
            contador = contador + 1

    def handler_bajar5_persona(self):
        contador = 0
        while contador<5:
            self.handler_bajar_persona()
            contador = contador + 1

    def handler_subirVarias_personas(self):
        cantidad = int(self.ventana.entradaNumero.text())
        contador = 0
        while contador<cantidad:
            self.handler_subir_persona()
            contador +=1

    def handler_bajarVarias_personas(self):
        cantidad = int(self.ventana.entradaNumero.text())
        contador = 0
        while contador<cantidad:
            self.handler_bajar_persona()
            contador +=1


    def actualizar_label (self):
        self.ventana.label.setText(str(self.auto.cantidad_personas))