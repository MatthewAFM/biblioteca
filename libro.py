from datetime import datetime, timedelta #Investigue acerca de las librerias, y en este caso utilice una libreria que nos ayuda a ver la fecha y hora de la computadora que estemos utlizando
                                            #Con eso nos vamos a guiar para ver la fecha de devolucion. 
class libro:
    def __init__(self, titulo, Autor, FechaDev, Prestado = False):
        self.__titulo = titulo
        self.__autor = Autor
        self.__prestado = Prestado
        self.__fechaDev = FechaDev

    def __str__(self):
        return f"El catalogo de libros es:{self.__titulo} {self.__autor} {self.__prestado} {self.__fechaDev}"
    
# Lista de libros con nombre, autor y estado de préstamo, en este caso muestra la cantidad de libros que tenemos y si estan prestados o no, si estan prestados muestra un dato TRUE y si no un FALSE
# Si no esta prestado, la fecha de devolucion la tomaria como None, y muestra en el listado N/A

    print("------------LIBROS DISPONIBLES Y NO DISPOBIBLES------------")
    print("En esta seccion se encuentran nuestros libros disponibles y los que estan alquilados")
libros = [
    {"nombre": "Cien años de soledad", "autor": "Gabriel García Márquez", "prestado": True, "fecha_devolucion": datetime.now() + timedelta(weeks=2)},
    {"nombre": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "prestado": False, "fecha_devolucion": None},
    {"nombre": "1984", "autor": "George Orwell", "prestado": True, "fecha_devolucion": datetime.now() + timedelta(weeks=2)},
    {"nombre": "Orgullo y prejuicio", "autor": "Jane Austen", "prestado": False, "fecha_devolucion": None},
    {"nombre": "El gran Gatsby", "autor": "F. Scott Fitzgerald", "prestado": True, "fecha_devolucion": datetime.now() + timedelta(weeks=2)},
    {"nombre": "Matar a un ruiseñor", "autor": "Harper Lee", "prestado": False, "fecha_devolucion": None},
    {"nombre": "Crónica de una muerte anunciada", "autor": "Gabriel García Márquez", "prestado": True, "fecha_devolucion": datetime.now() + timedelta(weeks=2)},
    {"nombre": "Los hermanos Karamazov", "autor": "Fiódor Dostoyevski", "prestado": False, "fecha_devolucion": None},
    {"nombre": "La sombra del viento", "autor": "Carlos Ruiz Zafón", "prestado": True, "fecha_devolucion": datetime.now() + timedelta(weeks=2)},
    {"nombre": "El código Da Vinci", "autor": "Dan Brown", "prestado": False, "fecha_devolucion": None}
]

# Imprimir la lista de libros
for libro in libros:
    estado = "Prestado" if libro["prestado"] else "Disponible"
    fecha = libro["fecha_devolucion"].strftime("%Y-%m-%d") if libro["prestado"] else "N/A"
    print(f"Nombre: {libro['nombre']}, Autor: {libro['autor']}, Estado: {estado}, Fecha de Devolución: {fecha}")
