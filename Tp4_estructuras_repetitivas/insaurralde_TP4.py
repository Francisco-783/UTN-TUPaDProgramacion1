import random

# ------------------------------
# Definición de funciones (TP4)
# ------------------------------

def ej1():
    for i in range(101):
        print(i)

def ej2():
    num = int(input("Ingresá un número entero: "))
    cantidad_digitos = len(str(abs(num)))
    print(f"El número tiene {cantidad_digitos} dígitos")

def ej3():
    a = int(input("Ingresá el primer número: "))
    b = int(input("Ingresá el segundo número: "))
    if a > b:
        a, b = b, a
    suma = 0
    for i in range(a + 1, b):
        suma += i
    print(f"La suma de los enteros entre {a} y {b} es {suma}")

def ej4():
    total = 0
    while True:
        num = int(input("Ingresá un número (0 para terminar): "))
        if num == 0:
            break
        total += num
    print(f"El total acumulado es {total}")

def ej5():
    secreto = random.randint(0, 9)
    intentos = 0
    while True:
        num = int(input("Adiviná el número (0-9): "))
        intentos += 1
        if num == secreto:
            print(f"¡Correcto! El número era {secreto}. Intentos: {intentos}")
            break
        else:
            print("Incorrecto, probá de nuevo.")

def ej6():
    for i in range(100, -1, -2):
        print(i)

def ej7():
    n = int(input("Ingresá un número entero positivo: "))
    if n < 0:
        print("Debe ser positivo.")
        return
    suma = sum(range(n + 1))
    print(f"La suma de 0 a {n} es {suma}")

def ej8():
    cantidad = 100  # cambiar este valor para pruebas
    pares = impares = positivos = negativos = 0

    for i in range(cantidad):
        num = int(input(f"Ingresá el número {i+1}: "))
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
        if num >= 0:
            positivos += 1
        else:
            negativos += 1

    print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")

def ej9():
    cantidad = 100  # cambiar este valor para pruebas
    numeros = []
    for i in range(cantidad):
        num = int(input(f"Ingresá el número {i+1}: "))
        numeros.append(num)
    media = sum(numeros) / cantidad
    print(f"La media de los números ingresados es {media}")

def ej10():
    num = input("Ingresá un número: ")
    invertido = num[::-1]
    print(f"Número invertido: {invertido}")

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
        print("\n=== TP4 - Hub de Ejercicios ===")
        for i in range(1, 11):
            print(f"{i}. Ejercicio {i}")
        print("0. Salir")

        eleccion = input("Elegí una opción: ")

        if eleccion == "0":
            print("Saliendo...")
            break
        elif eleccion in opciones:
            opciones[eleccion]()
        else:
            print("Opción inválida. Intente de nuevo.")

# ------------------------------
# Punto de entrada
# ------------------------------

if __name__ == "__main__":
    menu()
