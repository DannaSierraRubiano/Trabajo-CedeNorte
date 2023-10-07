#Crear una clase llamada persona que va a pedir: nombre, cedula, celular.
#1 metodo = "llamar persona" y tiene que mostrar un mensaje que diga "llamando a [nombre de la persona]"

class Pesona():
    def __init__(self, nombre, cedula, celular):
        self.nombre = nombre
        self.cedula = cedula
        self.celular = celular
    
    def LlamarPersona(self):
        print("Llamando a "+ self.nombre)

Persona_nombre = Pesona("Samantha", 1095, 30012)
Persona_nombre.LlamarPersona()
