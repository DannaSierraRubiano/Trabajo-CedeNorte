# class Vehiculo():
    
#     #Constructor, permite crear los objetos instanciados de esta clase
#     def __init__(self, ruedas, puertas, color, tipo = 'terrestre'):
#         self.ruedas = ruedas
#         self.puertas = puertas
#         self.color = color
#         self.tipo = tipo
    
#     def informacionVehiculo(self):
#         print("El vehiculo tiene "+ str(self.ruedas)+ " ruedas y tiene "+ str(self.puertas)+ " puertas y es de tipo " + self.tipo)

#     def arrancar(self):
#         print("El vehiculo esta arrancando")

# # Instanciando clase
# miMoto = Vehiculo(2, 0, "negro")

# # miMoto.informacionVehiculo()
# # miMoto.arrancar()

# elBarco = Vehiculo(0, 30, "Blanco", "acuatico")
# elBarco.informacionVehiculo()

# #Crear un método que se llame arrancar y que cuando lo llamen diga con un print "el vehiculo esta arrancando"

#Crear una clase llamada persona que va a pedir: nombre, cedula, celular.
#1 metodo = "llamar persona" y tiene que mostrar un mensaje que diga "llamando a [nombre de la persona]"

class Persona():
    def __init__(self, nombre, edad, cedula, celular):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
        self.celular = celular
    
    def LlamarPersona(self):
        print("Llamando a "+ self.nombre)

# Persona_nombre = Persona("Samantha", 28, 1095, 30012)
# Persona_nombre.LlamarPersona()

#Herencia
class Empleado(Persona):
    def __init__(self, nombre, edad, cedula, celular, empresa, cargo, sueldo):
        super().__init__(nombre, edad, cedula, celular)
        self.empresa = empresa
        self.cargo = cargo
        self.sueldo = sueldo

    def accionTrabajar(self):
        print("El trabajador "+ self.nombre + " está laborando...")

trabajador = Empleado("Carlos", 28, 1096235380, 3003143194, "Analitica SAS", "Ingeniero", 200)
trabajador.LlamarPersona()