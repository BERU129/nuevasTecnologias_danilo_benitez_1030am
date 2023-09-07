library = []

def add_book():
    print("**************BIENVENIDO A LA LIBRERIA************")
    book = input("ingrese el nombre del libro : ")
    library.append(book)
    print("!!!libro creado¡¡¡.")

def update_book():
    book = input("ingrese el nombre del libro que desea actualizar : ")
    if book in library:
        new_book = input("ingrese el nuevo nombre del libro : ")
        index = library.index(book)
        library[index] = new_book
        print("!!!libro Actualizado¡¡¡.")
    else:
        print("!!Libro no encontrado, CALVOO¡¡.")

def delete_book():
    book = input("ingrese el nombre del libro que desea eliminar : ")
    if book in library:
        library.remove(book)
        print("!!Libro eliminado¡¡ ** Procede a llorar **.")
    else:
        print("!!Libro no encotrado¡¡ BOBO.")

def list_books():
    if len(library) == 0:
        print("**No hay libro en la libreria/biblioteca.**")
    else:
        print("**Libros en la biblioteca actualmente**:")
        for book in library:
            print(book)

while True:
    print("\nELIJA UNA OPCION MI AMOR:")
    print("1. Agregar Libro")
    print("2. Actualizar Libro")
    print("3. Eliminar Libro")
    print("4. Listar Libros")
    print("5. Salida")

    choice = input("DIGITE EL NUMERO PARA ACCDER : ")

    if choice == "1":
        add_book()
    elif choice == "2":
        update_book()
    elif choice == "3":
        delete_book()
    elif choice == "4":
        list_books()
    elif choice == "5":
        break
    else:
        print("***eleccion no valida, intente de nuevo bobo.***")