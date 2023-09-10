#ciclo de vida

# import random 

# vidas = 5

# puntos = 0

#num = random.randint(0, 9)

# while (vidas != 0):

#     num = random.randint(0, 9)

#     if num == 0:
#         vidas-=1
#         print(f"vidas:{vidas}")
#     else:
#         puntos += 1
#         print(f"puntos:{puntos}")


#------------------------------------------------------------------------------

#SISTEMA DE VENTAS

# print("*********** Compras Don pepe***********")

# saldo = 15000
# precios = {"manzana": 2000, "pera": 3000, "banana": 3000, "Doritos": 7500,}
# # cuotas = 0

# while True:
#     print("Saldo actual:", saldo)
#     print("Productos disponibles:", list(precios.keys()))
#     producto = input("Ingrese el produco ('o' fin): ")
    
#     if producto == "fin":
#         break
    
#     if producto not in precios:
#         print("Producto no disponible")
#         continue
    
#     cantidad = int(input("cantidad : "))
#     costo = precios[producto] * cantidad
    
#     if saldo < costo:
#         print("Saldo insuficiente")
#         continue
    
#     saldo -= costo
#     print("Compra realizada. Saldo restante:", saldo)

#     print("*****Gracios por comprar******")

#-----------------------------------------------------------------------------

#REGISTRO DE USUARIO

# registro_usuario = []  

# def register():
#     name = input("Ingrese su Nombre: ")
#     email = input("Ingrese un correo: ")
#     phone = input("Ingrese Num Telefono: ")
#     password = input("Ingrese contraseña: ")
    
#     usuario = {'name': name, 'email': email, 'phone': phone, 'password': password}
#     registro_usuario.append(usuario)
#     print("***Registro completo****\n")

# def login():
#     email = input("Ingrese su correo: ")
#     phone = input("Ingrese su telefono: ")
    
#     for usuario in registro_usuario:
#         if usuario['email'] == email and usuario['phone'] == phone:
#             print("***inicio de sesion completo***\n")
#             return
#     print("Informacion incorreta, intente otra vez.\n")

# while True:
#     print("***********BIENVENIDO A LA TORRE AVENGERS***********")

#     print("Menu:")
#     print("1. Registrarse")
#     print("2. Login")
#     print("3. Exit")
    
#     choice = input("Ingrese el numero para accerder (1-3): ")
    
#     if choice == '1':
#         register()
#     elif choice == '2':
#         login()
#     elif choice == '3':
#         print("Saliendo...")
#         break
#     else:
#         print("mala eleccion intente otra vez CALVO.\n")

#--------------------------------------------------------------------------------------




