# Ejercicio condicional.
numero1 = input("¿Ingrese el primer número?: ");
numero2 = input("¿Ingrese el segundo número?: ");

print("Este es el número uno "+numero1+" este es el número dos "+numero2);

numero1 = int(numero1);
numero2 = int(numero2);

# Condicionales anidados, es decir, condicionales que están dentro de otros condicioanles. En este caso un if dentro de un else.

# if(numero1 == numero2):
#     print("Los números son iguales");
# else:
#     print("Los números no son iguales");
#     if(numero1>numero2):
#         print("El mayor es: "+ str(numero1));
#     else:
#         print("El mayor es: "+ str(numero2));

# Condicional elif
# numero1 = 2
# numero2 = 2

if (numero1 == numero2):
    print("Los números son iguales")
elif(numero1 < 0):
    print("El número es el "+ str(numero1)+" es negativo")
elif(numero2<0):
     print("El número es el "+ str(numero2)+" es negativo")
else:
    print("Ningun número es negativo")
print("Fin de la llamada")