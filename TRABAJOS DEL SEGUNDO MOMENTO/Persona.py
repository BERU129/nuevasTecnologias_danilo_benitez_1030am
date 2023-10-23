class Persona:
    def _init_(self, nombre, edad, genero, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.ciudad = ciudad

    def presentarse(self):
        return f"¡Hola! Mi nombre es {self.nombre}, tengo {self.edad} años, soy {self.genero} y vivo en {self.ciudad}."

persona1 = Persona("Juan", 30, "Masculino", "Ciudad A")
print(persona1.presentarse())