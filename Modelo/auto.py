# -*- coding: utf-8 -*-
class Auto():

    def __init__(self):
        self.cantidad_personas = 0

    def subir_persona(self):
        self.cantidad_personas +=1

    def bajar_persona(self):
        self.cantidad_personas -=1

mi_auto = Auto()
print mi_auto.cantidad_personas
mi_auto.subir_persona()
mi_auto.subir_persona()
print mi_auto.cantidad_personas
mi_auto.bajar_persona()
print mi_auto.cantidad_personas