#Hay tres ciclos: 1. While (Mientras) El ciclo se ejecuta un bloque de código que haya una condición que le detenga.

condicion = True
while(condicion):
    print("Bloque de código a ejecutar")
    condición = input("¿Quiere que se detenga?")
    if(condicion.upper() == 'SI'): #.upper -> "sI, si, Si" igualmente se detiene.
        condicion = False #Break (Romper el ciclo)

#Van a hacer un contador del 1 al 10 y que se detenga.
a = 0
while(a < 11): #Para que se ejecute el valor debe ser menor a 11 o sea False hasta que sea True (10).
    print(a)
    a = a + 1

condicion = True
contador = 0
while(condicion):
    print(contador)
    contador = contador+1
    if(contador > 10):
        break

Contador=0
while(Contador<=10):
    print(Contador)
    Contador=Contador+1

i = 0
while i<10:
	i = i+1
	print(i)

# Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.
suma = 0
while (True):
    numero = int(input("ingrese un número:  "))
    suma = suma + numero
    if(numero == 0):
        print("La suma es: "+str(suma))
        break

# Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0.
# Informar cuál fue el mayor número ingresado.

# Inicializamos la variable para almacenar el número mayor con un valor negativo
numero_mayor = -1

while True:
    # Solicitamos al usuario que ingrese un número entero
    entrada = input("Ingrese un número entero positivo (o 0 para salir): ")

    # Intentamos convertir la entrada en un número entero
    try:
        numero = int(entrada)
    except ValueError:
        print("Entrada inválida. Ingrese un número entero positivo.")
        continue

    # Verificamos si el número ingresado es 0 para salir del bucle
    if numero == 0:
        break

    # Verificamos si el número ingresado es positivo
    if numero > 0:
        # Comparamos con el número mayor actual y actualizamos si es mayor
        if numero > numero_mayor:
            numero_mayor = numero
    else:
        print("Número no válido. Ingrese un número entero positivo.")

# Mostramos el número mayor ingresado
if numero_mayor != -1:
    print(f"El número mayor ingresado fue: {numero_mayor}")
else:
    print("No se ingresaron números enteros positivos.")
