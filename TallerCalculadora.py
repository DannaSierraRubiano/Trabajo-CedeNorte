print("Bienvenido a la calculadora");

number1 = int(input("Ingrese el primer número: "));
operacion = input("Ingrese un signo: ")
number2 = int(input("Ingrese el segundo número: "));

if(operacion == '+'):
    print("El resultado es: " + str(number1+number2))
elif(operacion == '-'):
    print("El resultado es: " + str(number1-number2))
elif(operacion == '*'):
    print("El resultado es: " + str(number1*number2))
elif(operacion == '/'):
    print("El resultado es: " + str(number1/number2))
else:
    print("Ingrese una operación correcta")

print("Fin del programa, hasta luego.");