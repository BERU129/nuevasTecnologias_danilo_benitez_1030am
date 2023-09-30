class Persona:

    compania = "xyz"

    def __init__ (self, id, nombre, correo, contraseña):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña

    def verPersona(self):
        print(f"Id:{self.id} \n",
              f"Nombre:{self.nombre} \n",
              f"Correo:{self.correo} \n",
              f"Compañia:{self.compania}")


maria= Persona(1, "Maria", "Maria@gmail", "qwe123")

maria.verPersona()

maria.correo = "nperez@gmail.com"