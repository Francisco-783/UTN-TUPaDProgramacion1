import math

# ------------------------------
# Definición de funciones (ejercicios)
# ------------------------------

def ej1():
    print("Hola Mundo!")

def ej2():
    nombre = input("Ingresá tu nombre: ")
    print(f"Hola {nombre}!")

def ej3():
    nombre = input("Ingresá tu nombre: ")
    apellido = input("Ingresá tu apellido: ")
    edad = input("Ingresá tu edad: ")
    residencia = input("Ingresá tu lugar de residencia: ")
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

def ej4():
    radio = float(input("Ingresá el radio del círculo: "))
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
    print(f"Área: {area:.2f}, Perímetro: {perimetro:.2f}")

def ej5():
    segundos = int(input("Ingresá una cantidad de segundos: "))
    horas = segundos / 3600
    print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

def ej6():
    num = int(input("Ingresá un número: "))
    print(f"Tabla del {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")

def ej7():
    a = int(input("Ingresá el primer número (≠ 0): "))
    b = int(input("Ingresá el segundo número (≠ 0): "))
    print(f"Suma: {a + b}")
    print(f"Resta: {a - b}")
    print(f"Multiplicación: {a * b}")
    print(f"División: {a / b}")

def ej8():
    peso = float(input("Ingresá tu peso en kg: "))
    altura = float(input("Ingresá tu altura en metros: "))
    imc = peso / (altura ** 2)
    print(f"Tu IMC es: {imc:.2f}")

def ej9():
    celsius = float(input("Ingresá la temperatura en °C: "))
    fahrenheit = (9/5) * celsius + 32
    print(f"{celsius} °C equivalen a {fahrenheit:.2f} °F")

def ej10():
    n1 = float(input("Ingresá el primer número: "))
    n2 = float(input("Ingresá el segundo número: "))
    n3 = float(input("Ingresá el tercer número: "))
    promedio = (n1 + n2 + n3) / 3
    print(f"El promedio es: {promedio:.2f}")

# ------------------------------
# Menú principal (hub)
# ------------------------------

def menu():
    opciones = {
        "1": ej1,
        "2": ej2,
        "3": ej3,
        "4": ej4,
        "5": ej5,
        "6": ej6,
        "7": ej7,
        "8": ej8,
        "9": ej9,
        "10": ej10
    }

    while True:
        print("\n=== TP1 - Hub de Ejercicios ===")
        for i in range(1, 11):
            print(f"{i}. Ejercicio {i}")
        print("0. Salir")

        eleccion = input("Elegí una opción: ")

        if eleccion == "0":
            print("Saliendo...")
            break
        elif eleccion in opciones:
            opciones[eleccion]()  # ejecuta la función correspondiente
        else:
            print("Opción inválida. Intente de nuevo.")

# ------------------------------
# Punto de entrada
# ------------------------------

if __name__ == "__main__":
    menu()