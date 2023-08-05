accion = input("""Ingrese la opción:
1- Registro
2- Login
Seleccione el numero que desea de la opción: """);

usuarioRegistrado = "barbie"
contraseñaRegistrado = "contraseña"

if(accion == "2"):
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if(usuario == usuarioRegistrado and contraseña == contraseñaRegistrado):
        print("Usuario logeado correctamente!!")
    else:
        print("Verifique sus datos")