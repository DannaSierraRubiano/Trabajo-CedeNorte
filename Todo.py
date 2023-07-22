# Imprimiendo hola mundo
print("Hola Mundo!")
print("Nueva información en la lobby")

texto = "Esto es un texto dos";
print(texto);

# Concatenando textos
texto1 = "James";
texto2 = "Lozada";
# Se concatenó el texto1 y el texto2, es decir, se unieron
texto3 = texto1+" "+texto2;
print(texto3);

print("Ejercicio 2!")
#Creando variables con número

variable1 = 2;
variable2 = 10;
variable3 = "2";

var01 = variable1+variable2;
var02 = variable3+ variable2;

print(var01);
print(var02);

# Creando variables.
var1 = 2;
var2 = 3;
var3 = 3;

if (var1 == var2):
     print("Los números son iguales")
else:
     print("Los números no son iguales");

if (var2 == var3):
     print("Los números son iguales")
else:
     print("Los números no son iguales");

# Ejercicio condicional.
numero1 = input("Ingrese el primer número: ");
numero2 = input("Ingrese el segundo número: ");

print("Este es el número uno "+numero1+" este es el número dos "+numero2);

numero1 = int(numero1);
numero2 = int(numero2);

# Condicionales anidados, es decir, condicionales que están dentro de otros condicioanles. En este caso un if dentro de un else.
if(numero1 == numero2):
    print("Los números son iguales");
else:
    print("Los números no son iguales");
    if(numero1>numero2):
        print("El mayor es: "+ str(numero1));
    else:
        print("El mayor es: "+ str(numero2));

# Condicional elif
if (numero1 == numero2):
    print("Los números son iguales")
elif(numero1 < 0):
    print("El número es el "+ str(numero1)+" es negativo")
elif(numero2<0):
     print("El número es el "+ str(numero2)+" es negativo")
else:
    print("Ningun número es negativo")
print("Fin de la llamada")

#Calculadora
print("Bienvenido a la calculadora");

number1 = int(input("Ingrese el primer número: "));
number2 = int(input("Ingrese el segundo número: "));

print("Escoja una de las siguientes operaciones")
print("1- Ingrese el número 1, si desea sumar")
print("2- Ingrese el número 2, si desea restar")
print("3- Ingrese el número 3, si desea multiplicar")
print("4- Ingrese el número 4, si desea dividir")

operacion = input("Ingrese su operación: ")

if(operacion == '1'):
    print("El resultado es: " + str(number1+number2))
elif(operacion == '2'):
    print("El resultado es: " + str(number1-number2))
elif(operacion == '3'):
    print("El resultado es: " + str(number1*number2))
elif(operacion == '4'):
    print("El resultado es: " + str(number1/number2))
else:
    print("Ingrese una operación correcta")

print("Fin del programa, hasta luego.");
