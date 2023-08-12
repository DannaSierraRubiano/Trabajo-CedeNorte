#Usuario ya registrado
usuario_registrado = "Lucas"
contrasena_registrada = "12"

#Hora actual
import datetime

hora_actual = datetime.datetime.now()
print(hora_actual.strftime('%I:%M de %d/ %m/ %y'))

#Inicio
print("----------------------------------------")
print ("""      Bienvenido a la interfaz
       Ingrese sus credenciales""")

print("""1 = Ingrese su usuario
2 = Ingrese por Microsoft""")

entrada = input()

if(entrada == "1"): #Login
    print("Usuario:")
    Usuario = input()
    print("Contraseña:")
    Contrasena = input()
    if (Usuario == usuario_registrado and Contrasena == contrasena_registrada): #Identifica al usuario
        print("Ingresando...")
        if __name__ == '__main__':
          print("¿Cuantos clientes quieres registrar?: ") #Registro de clientes
          nclientes = int(input())
          contador = 0
          usuario_nombre = [str() for ind0 in range(nclientes)]
          usuario_apellido = [str() for ind0 in range(nclientes)]
          usuario_edad = [float() for ind0 in range(nclientes)]
          usuario_cedula = [float() for ind0 in range(nclientes)]
          usuario_telefono = [float() for ind0 in range(nclientes)]
          
          while contador < nclientes:
            contador = contador + 1
            print("Ingrese el nombre del cliente: ")
            nombre = input()
            usuario_nombre[contador-1] = nombre
            print("Ingrese el apellido del cliente: ")
            apellido = input()
            usuario_apellido[contador-1] = apellido
            print("Ingrese el edad del cliente: ")
            edad = input()
            usuario_edad[contador-1] = edad
            print("Ingrese el cedula del cliente: ")
            cedula = input()
            usuario_cedula[contador-1] = cedula
            print("Ingrese el telefono del cliente: ")
            telefono = input()
            usuario_telefono[contador-1] = telefono
            print("----------------------------------------")
        contador = 0
        while contador<nclientes: #Información de los clientes registrados
                contador = contador+1
                print(" El nombre del cliente es:",usuario_nombre[contador-1])
                print(" El apellido del cliente es: ", usuario_apellido[contador-1]) 
                print(" La edad del cliente es: ", usuario_edad[contador-1]) 
                print(" La cedula del cliente es: ", usuario_cedula[contador-1]) 
                print(" El telefono del cliente es: ", usuario_telefono[contador-1])
                print("----------------------------------------")
    else:
        print("Usuario o contraseña son inválidos") #No se identifico al usuario
elif(entrada == "2"):
    print("Ingresando por medio de Microsoft...") #OAuth
else:
    print("__Verifique sus datos__") #Se ingreso un número invalido

#Hora actual
import datetime

hora_actual = datetime.datetime.now()
print(hora_actual.strftime('%I:%M de %d/ %m/ %y'))

print("----------------------------------------")
import time

#Cronometro antes de volver a iniciar la secuencia
def cronometro(tiempo_segundos):
    tiempo_inicial = time.time()
    tiempo_final = tiempo_inicial + tiempo_segundos
    
    while time.time() < tiempo_final:
        tiempo_restante = int(tiempo_final - time.time())
        minutos = tiempo_restante // 60
        segundos = tiempo_restante % 60
        print(f"Tiempo restante: {minutos:02d}:{segundos:02d}", end="\r")
        time.sleep(1)
    
    print("¡Tiempo completado!")

tiempo_minutos = 0.2
tiempo_segundos = tiempo_minutos * 60
cronometro(tiempo_segundos)