def tabla(n, hasta=10):
    for i in range(1, hasta+1):
        print(f"{n} x {i} = {n*i}")

def main():
    try:
        n = int(input("Número para tabla: "))
        hasta = int(input("Hasta (ej. 10): "))
        tabla(n, hasta)
    except ValueError:
        print("Introduce números enteros válidos.")

if __name__ == "__main__":
    main()
