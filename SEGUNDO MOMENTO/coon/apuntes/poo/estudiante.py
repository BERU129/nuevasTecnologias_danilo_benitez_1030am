from coon.apuntes.poo.persona import Persona


class Estudiante(Persona):

    def __int__(self, id, nombre, correo, contraseña, programa, semestre):
        super().__init__(id, nombre, correo, contraseña)
        self.programa = programa
        self.semestre = semestre

    def verPersona(self):
        print(f"Id:{self.id} \n",
              f"Nombre:{self.nombre} \n",
              f"Correo:{self.correo} \n",
              f"Compañia:{self.compania}",
              f"Programa: {self.programa} \n",
              f"Semestre:{self.semestre}")


estudiante1 = Estudiante(1, "maria", "gus@gmail", "12345", "sofware", 1)

print(estudiante1.programa)