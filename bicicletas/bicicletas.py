#PROFE OPTE POR HACERLO CON WHILE ESPERO Y LE GUSTE 
#Danilo Esteban Benitez Lopez : 1030Am

usuarios = []
prestamo = []

while True:
    print("*******BIENVENIDO A LAS CILAS DE DON PATRISIO******")

    print("**Seleccione una opción**:")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Prestar una bicicleta")
    print("4. Consultar usuarios registrados")
    print("5. Consultar préstamos realizados")
    print("6. Salir")

    option = input("**Ingrese su opción**: ")

    if option == "1":
        name = input("Ingrese nombre usuario: ")
        card_number = input("Ingrese número de tarjeta: ")
        usuarios.append({"name": name, "card_number": card_number})
        print("!!!Usuario registrado exitosamente¡¡¡.")

    elif option == "2":
        card_number = input("Ingrese el número de tarjeta: ")
        user = next((user for user in usuarios if user["card_number"] == card_number), None)
        if user:
            print(f"***Bienvenido, {user['name']}***!")
        else:
            print("!!!Lo siento, no se encontró su número de tarjeta en la base de datos.¡¡¡")

    elif option == "3":
        card_number = input("Ingrese el número de tarjeta: ")
        user = next((user for user in usuarios if user["card_number"] == card_number), None)
        if user:
            origin = input("Ingrese el origen de la bicicleta: ")
            destination = input("Ingrese el destino de la bicicleta: ")
            prestamo.append({"user": user, "origin": origin, "destination": destination})
            print("!!!Préstamo realizado¡¡¡.")
        else:
            print("!!!SORRYY, no se encontró su número de tarjeta en la base de datos¡¡¡.")

    elif option == "4":
        print(f"***Hay {len(usuarios)} usuarios registrados¡¡¡.")

    elif option == "5":
        print(f"!!!Se han realizado {len(prestamo)} préstamos.¡¡¡")

    elif option == "6":
        break

    else:
        print("Opción inválida. Inténtelo de nuevo.")