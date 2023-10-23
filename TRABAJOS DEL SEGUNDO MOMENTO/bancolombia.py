employees = {}


def add_employee():
    id = input("Ingrese el ID: ")
    name = input("Ingrese el nombre: ")
    last_name = input("Ingrese el apellido: ")
    position = input("Ingrese la posicion, empleado o supervisor : ")
    area = input("Ingrese el area: ")
    salary = float(input("Ingrese el salario: "))

    if salary < 2 * 908526:
        net_salary = salary + 106454
    else:
        net_salary = salary

    employees[id] = {"name": name, "last_name": last_name, "position": position, "area": area, "salary": salary, "net_salary": net_salary}

    print("***Agregado con Exito****.")

def list_employees():
    if len(employees) == 0:
        print("****No hay usuarios registrados en el sistema****.")
    else:
        # MOSTRAMOS EN FILA PARA QUE SE VEA MAS ORGANIZADO
        print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID", "Nombre", "Apellido", "Posicion", "Area", "Salario"))

        for id, employee in employees.items():
            print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20.2f}".format(id, employee["name"], employee["last_name"], employee["position"], employee["area"], employee["salary"]))

def print_payslip():
    id = input("***Ingrese el ID del empleado o supervisor para ver la nomina*** : ")

    if id in employees:
        print("Recibo de nomina :", id)
        print("Nombre:", employees[id]["name"], employees[id]["last_name"])
        print("Posicion:", employees[id]["position"])
        print("Area:", employees[id]["area"])
        print("Salario:", employees[id]["salary"])
        print("Salario neto:", employees[id]["net_salary"])
    else:
        print("El empleado o supervisor no existen.")

def view_employees():
    if len(employees) == 0:
        print("***No hay empleados registrados en el sistema***.")
    else:
        #MOSTRAMOS EN FILA PARA QUE SE VEA MAS ORGANIZADO
        print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID", "Nombre", "Apellido", "Posicion", "Area", "Salario"))

        for id, employee in employees.items():
            print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20.2f}".format(id, employee["name"], employee["last_name"], employee["position"], employee["area"], employee["salary"]))

def main():
    while True:
        print("******SISTEMA DE BANCOLOMBIA********")
        print("1. Agregar empleado/supervisor")
        print("2. Listar")
        print("3. Ver Nomina")
        print("4. Ver emplados(Solo supervisor@)")
        print("5. Salir")

        choice = input("Ingrese el numero : ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            list_employees()
        elif choice == "3":
            print_payslip()
        elif choice == "4":
            position = input("*+Ingrese su posicion** : ")
            if position.lower() == "supervisor":
                view_employees()
            else:
                print("***No tienes permiso para ver a los emplados***.")
        elif choice == "5":
            break
        else:
            print("*Intente otra vez*.")

if __name__ == "__main__":
    main()