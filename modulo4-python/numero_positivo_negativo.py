#Indicador de números positivos y negativos simple
def main():
    try:
        n = float(input("Ingresa un número: "))
        if n > 0:
            print("Positivo")
        elif n < 0:
            print("Negativo")
        else:
            print("Cero")
    except ValueError:
        print("Introduce un número válido.")

if __name__ == "__main__":
    main()
