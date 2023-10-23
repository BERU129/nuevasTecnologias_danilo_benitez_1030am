products = {}


def agregar_producto():
    id = input("Ingrese el ID: ")
    name = input("Ingrese el Nombre: ")
    cost = float(input("Ingrese el costo: "))
    quantity = int(input("Ingrese la cantidad: "))
    margin = float(input("Ingrese Margen de ganancia: "))

    price = cost / (1 - margin)
    inventory_value = quantity * cost

    products[id] = {"name": name, "cost": cost, "quantity": quantity, "margin": margin, "price": price,
                    "inventory_value": inventory_value}

    print("*****Producto Agregado Exitosamente*****.")


def listar_producto():
    if len(products) == 0:
        print("***No hay productos registrados en el sistema***.")
    else:
        # PROFE LO IMPRIMIMOS EN FILA PARA QUE SE VEA MAS ORGANIZADO
        print("{:<10} {:<20} {:<10} {:<10} {:<10} {:<20}".format("ID", "Nombre", "Costo", "Cantidad", "Margen", "Precio"))

        for id, product in products.items():
            print("{:<10} {:<20} {:<10.2f} {:<10} {:<10.2f} {:<20.2f}".format(id, product["name"], product["cost"],
                                                                              product["quantity"], product["margin"],
                                                                              product["price"]))


def actulizar_producto():
    id = input("Ingrese el ID del producto que desea Actualizar: ")

    if id in products:
        name = input("Ingrese el nuevo nombre : ")
        cost = input("Ingrese en nuevo costo : ")
        quantity = input("Ingrese la nueva cantidad : ")
        margin = input("Ingrese nueva margen de ganancia : ")

        if name != "":
            products[id]["name"] = name
        if cost != "":
            products[id]["cost"] = float(cost)
            products[id]["price"] = products[id]["cost"] / (1 - products[id]["margin"])
            products[id]["inventory_value"] = products[id]["quantity"] * products[id]["cost"]
        if quantity != "":
            products[id]["quantity"] = int(quantity)
            products[id]["inventory_value"] = products[id]["quantity"] * products[id]["cost"]
        if margin != "":
            products[id]["margin"] = float(margin)
            products[id]["price"] = products[id]["cost"] / (1 - products[id]["margin"])

        print("****Producto Actualizado exitosamente****.")
    else:
        print("**Producto no encontrado.**")


def main():
    while True:
        print("*******MINI TIENDA*******")
        print("1. Agregar producto")
        print("2. Listar producto")
        print("3. Actualizar Producto")
        print("4. Salir")

        choice = input("Ingrese un numero: ")

        if choice == "1":
            agregar_producto()
        elif choice == "2":
            listar_producto()
        elif choice == "3":
            actulizar_producto()
        elif choice == "4":
            break
        else:
            print("Intete otra vez.")


if __name__ == "__main__":
    main()
