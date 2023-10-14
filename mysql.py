import pymysql.cursors

class BaseDatos:
    def __init__(self):
        self.host = "localhost"
        self.usuario = "root"
        self.contrasena = "root"
        self.basededatos = "EjercicioPOO"
    
    def conectarBaseDatos(self): #ControlDeErrores
        try:
            connection = pymysql.connect(host=self.host,
                             user= self.usuario,
                             password= self.contrasena,
                             database= self.basededatos,
                             cursorclass=pymysql.cursors.DictCursor)
            print("¡Conexión establecida!")
            return connection
        except:
            print("Hay un fallo cuando se conecta a la base de datos")
    def escribirQuery(self, query, conexion):
        try:
            cursor = conexion.cursor()
            cursor.execute(query)
            print(cursor.fetchall())
            # return cursor.fetchall()
        except:
            print("Fallo cursor")

### Clase empleado

class Empleado:
    def __init__(self, nombre, salario, edad):
        self.nombre = nombre
        self.salario = salario
        self.edad = edad
    
    def agregarEmpleado(self, conexion):
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO empleados(nombre, salario, edad) VALUES ('"+self.nombre+"', "+str(self.salario)+", "+str(self.edad)+")")
        return "¡Empleado agregado correctamente!"

### Clase gestor de empleados
class GestorEmpleados:
    def agregarEmpleado(self, conexion):
        print("Seleccionó la opción de agregar empleados")

        print("Ingrese los siguientes datos:")
        nombre = input("Ingrese el nombre del empleado:  ")
        salario = input("Ingrese el salario del empleado:  ")
        edad = input("Ingrese el edad del empleado:  ")
        
        empleado = Empleado(nombre, salario, edad)
        mensaje = empleado.agregarEmpleado(conexion);
        if(mensaje != ''):
            print(mensaje)

### Se instancia la base de datos
basedatos = BaseDatos();
### Se conecta ala base de datos
conexion = basedatos.conectarBaseDatos()

empleado = Empleado("Juan",20000, 15)
mensaje =empleado.agregarEmpleado(conexion)
basedatos.escribirQuery("SELECT * FROM empleados", conexion)