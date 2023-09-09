#Registro de un nombre, número de identidad y edad. Esa edad van a mirar si es mayor o menor de edad.

def Registro(Nombre, Id, Edad):
    if (Edad<"18"):
        print(Nombre+" con numero de TI: "+Id+" Es menor de edad, porque tiene "+Edad+" años.")
    elif(Edad>"18"):
        print(Nombre+" con numero de CD: "+Id+" Es mayor de edad, porque tiene "+Edad+" años.")
    else:
        print(Nombre+" con numero de CD: "+Id+" Es mayor de edad, porque tiene "+Edad+" años.")

A=input("Ingrese el nombre: ")
B=input("Ingrese la CC/TI: ")
C=input("Ingrese la edad: ")
Registro(A,B,C)