#En esta seccion le pedimos los datos al lector.
def pedir_datos_personales():
    # Pedir los datos al usuario
    nombreApellido = input("Ingrese su nombre y su apellido: ")
    carnet = input("Ingrese su carnet: ")
    fecha_nacimiento = input("Ingrese su fecha de nacimiento (DD-MM-YYYY): ")

    # Mostrar los datos ingresados
    print("\nDatos ingresados:")
    print(f"Nombre: {nombreApellido}")
    print(f"Carnet: {carnet}")
    print(f"Fecha de nacimiento: {fecha_nacimiento}")

# Llamar a la función para pedir los datos
pedir_datos_personales()
#Este seria un menu el cual daria la opcion al usuario que ingreso si desea eliminar o agregar un libro
# Pero no supe muy bien como poder agregarlo para que llame la opcion desde libro.py            
def menu():
        while True:
            print("\Seleccione una opcion ")
            print("1. agregar un libro")
            print("2. Eliminar un libro")
            opcion = input("Seleccione una opcion")

            if opcion == 1:
               # libro.agregarlibro()
                break
            elif opcion == 2:
                eleminarlibro()
                break
            else:
                print("Ingrese una opcion valida")
