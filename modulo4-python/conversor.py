def c_to_f(c): return (c * 9/5) + 32
def f_to_c(f): return (f - 32) * 5/9
def clp_to_usd(clp, tasa=900.0): return clp / tasa
def usd_to_clp(usd, tasa=900.0): return usd * tasa

def main():
    print("1) C -> F  2) F -> C  3) CLP -> USD  4) USD -> CLP")
    op = input("Selecciona opción: ")
    try:
        if op == "1":
            c = float(input("Celsius: "))
            print(f"{c} °C = {c_to_f(c):.2f} °F")
        elif op == "2":
            f = float(input("Fahrenheit: "))
            print(f"{f} °F = {f_to_c(f):.2f} °C")
        elif op == "3":
            clp = float(input("CLP: "))
            print(f"{clp} CLP = {clp_to_usd(clp):.2f} USD (tasa por defecto)")
        elif op == "4":
            usd = float(input("USD: "))
            print(f"{usd} USD = {usd_to_clp(usd):.2f} CLP (tasa por defecto)")
        else:
            print("Opción inválida")
    except ValueError:
        print("Entrada inválida. Intenta con números.")

if __name__ == "__main__":
    main()
