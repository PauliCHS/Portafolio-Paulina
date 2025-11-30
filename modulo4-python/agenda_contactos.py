agenda = {}

def agregar():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    agenda[nombre] = telefono
    print("Contacto agregado.")

def listar():
    if not agenda:
        print("Agenda vacía.")
    for nombre, tel in agenda.items():
        print(f"{nombre}: {tel}")

def eliminar():
    nombre = input("Nombre a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print("Eliminado.")
    else:
        print("No encontrado.")

def main():
    while True:
        print("\n1) Agregar 2) Listar 3) Eliminar 4) Salir")
        op = input("Opción: ")
        if op == "1": agregar()
        elif op == "2": listar()
        elif op == "3": eliminar()
        elif op == "4": break
        else: print("Opción inválida")

if __name__ == "__main__":
    main()

