import math

def area_circulo(r): return math.pi * r * r
def area_triangulo(b, h): return (b * h) / 2
def area_cuadrado(a): return a * a

def main():
    print("1) Círculo 2) Triángulo 3) Cuadrado")
    op = input("Opción: ")
    try:
        if op == "1":
            r = float(input("Radio: "))
            print(f"Área: {area_circulo(r):.2f}")
        elif op == "2":
            b = float(input("Base: "))
            h = float(input("Altura: "))
            print(f"Área: {area_triangulo(b,h):.2f}")
        elif op == "3":
            a = float(input("Lado: "))
            print(f"Área: {area_cuadrado(a):.2f}")
        else:
            print("Opción inválida")
    except ValueError:
        print("Entrada inválida.")

if __name__ == "__main__":
    main()

