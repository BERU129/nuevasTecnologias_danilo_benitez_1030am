class Product:
    def __init__(self, id, name, description, cost, quantity, margin):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.quantity = quantity
        self.margin = margin
        self.price = 0

    def register_product(self, callback):
        self.price = self.cost / (1 - self.margin)
        callback(self)

    @staticmethod
    def print_product_list(products):
        for product in products.values():
            print(f"ID: {product.id}")
            print(f"Nombre: {product.name}")
            print(f"Descripcion: {product.description}")
            print(f"Costo: {product.cost}")
            print(f"Cantidad: {product.quantity}")
            print(f"Precio: {product.price}")
            print("------------------------------")

    @staticmethod
    def register_product_from_console():
        id = int(input("Ingrese el id ID: "))
        name = input("Ingrese el nombre del producto: ")
        description = input("ingrese la descripcio: ")
        cost = float(input("ingrese el costo: "))
        quantity = int(input("ingrese la cantidad: "))
        margin = float(input("ingrese el margen: "))

        product = Product(id, name, description, cost, quantity, margin)
        product.register_product(assign_price)

        products[product.id] = product


products = {}


def assign_price(product):
    product.price = product.cost / (1 - product.margin)


Product.register_product_from_console()


Product.print_product_list(products)
