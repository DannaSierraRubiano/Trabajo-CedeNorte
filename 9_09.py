# Poder registrar información como nombre, número de identificación, que compró y cuanto gasto en total.

#Funciones
def registrar_cliente (cedula):
    cedulas.append(cedula)
    nombre=input("Ingrese su nombre: ")
    nombres.append(nombre)
    print("Cliente registrado correctamente")

nombres = []
cedulas = []
compras = []
totales = []

# var_nombre = input("Ingrese el nombre: ")
# nombres.append (var_nombre)
# var2_nombre = input("Ingrese otro nombre: ")
# nombres.append (var2_nombre)
# print(nombres)

# contador = 0
# while (contador<10):
#     contador += 1
#     print(contador)

while (True):
    print("~~ Bienvenido a su sistema de gestion del mercadeo ~~")
    print("Por favor seleccione una de las siguientes opciones")
    print("""Escriba: 
          '1-' si deseas registrar una nueva compra
          '2-' si deseas consultar las compras de ese cliente
          '3-' si deseas editar la información del cliente
          '4-' si desea ver la información del cliente
          '5-' si desea apagar el sistema""")
    opcion = input("Ingrese la opción solicitada: ")
    if(opcion=="1"):
        print("Registrando una nueva compra")
        cedula =input("Ingrese su cedula: ")
        if((cedula in cedulas)==False):
            registrar_cliente(cedula) #Agregando cedula
            productos=input("Ingrese los productos separados por coma (,): ")
            arr_productos=productos.split (",")
            compras.append (arr_productos)
        else:
            posicion=cedulas.index(cedula)
            productos=input("Ingrese los productos separados por coma(,): ").split(",")
            if(len(compras[posicion])==0):
                compras[posicion]=productos
            else:
                compras[posicion] += productos
            print(compras)
    elif(opcion=="2"):
        print("Consultando compras del cliente: ")
    elif(opcion=="3"):
        print("Editando información del cliente: ")
    elif(opcion=="4"):
        print("Mostrando información del cliente: ")
        if(len(cedulas)!=0):
            cedula = input("Ingresa la cedula que deseas ver:  ")
            if((cedula in cedulas)==True):
                print(" -- El nombre del cliente es:  "+nombres[cedulas.index(cedula)]+ " identificado con la cedula:  "+cedula)
            else:
                print("Registrando al cliente...")
                registrar_cliente(cedula)
    elif(opcion=="5"):
        print("Apagando el sistema...")
    else:
        print("¡Opción incorrecta! Ingrese una nueva opción...")


