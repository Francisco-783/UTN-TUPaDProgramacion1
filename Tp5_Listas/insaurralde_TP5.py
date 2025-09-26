import random

# ------------------------------
# Definición de funciones (TP5)
# ------------------------------

def ej1():
    notas = [random.randint(1, 10) for _ in range(10)]
    print("Notas de los estudiantes:")
    for n in notas:
        print(n)
    promedio = sum(notas) / len(notas)
    print(f"Promedio: {promedio:.2f}")
    print(f"Nota más alta: {max(notas)}")
    print(f"Nota más baja: {min(notas)}")

def ej2():
    productos = []
    for i in range(5):
        productos.append(input(f"Ingresá el producto {i+1}: "))

    print("Lista ordenada alfabéticamente:")
    for p in sorted(productos):
        print(p)

    eliminar = input("¿Qué producto desea eliminar? ")
    if eliminar in productos:
        productos.remove(eliminar)
        print("Lista actualizada:")
        for p in productos:
            print(p)
    else:
        print("Ese producto no está en la lista.")

def ej3():
    numeros = [random.randint(1, 100) for _ in range(15)]
    pares = [n for n in numeros if n % 2 == 0]
    impares = [n for n in numeros if n % 2 != 0]

    print(f"Números: {numeros}")
    print(f"Pares ({len(pares)}): {pares}")
    print(f"Impares ({len(impares)}): {impares}")

def ej4():
    lista = [1, 2, 2, 3, 4, 4, 5, 1, 6]
    sin_repetidos = list(set(lista))
    print(f"Original: {lista}")
    print(f"Sin repetidos: {sin_repetidos}")

def ej5():
    estudiantes = ["Ana", "Juan", "Pedro", "Lucía", "María", "Carlos", "Sofía", "Diego"]
    print("Estudiantes actuales:", estudiantes)

    opcion = input("¿Querés agregar (A) o eliminar (E) un estudiante?: ").upper()
    if opcion == "A":
        nuevo = input("Nombre del estudiante a agregar: ")
        estudiantes.append(nuevo)
    elif opcion == "E":
        borrar = input("Nombre del estudiante a eliminar: ")
        if borrar in estudiantes:
            estudiantes.remove(borrar)
        else:
            print("Ese estudiante no está en la lista.")
    else:
        print("Opción inválida.")

    print("Lista final de estudiantes:", estudiantes)

def ej6():
    lista = [1, 2, 3, 4, 5, 6, 7]
    print("Lista original:", lista)
    rotada = [lista[-1]] + lista[:-1]
    print("Lista rotada:", rotada)

def ej7():
    temperaturas = [
        [10, 20],
        [12, 22],
        [8, 18],
        [15, 25],
        [11, 23],
        [9, 21],
        [14, 24]
    ]
    minimas = [dia[0] for dia in temperaturas]
    maximas = [dia[1] for dia in temperaturas]
    promedio_min = sum(minimas) / len(minimas)
    promedio_max = sum(maximas) / len(maximas)

    print(f"Promedio mínimas: {promedio_min:.2f}")
    print(f"Promedio máximas: {promedio_max:.2f}")

    amplitudes = [maximas[i] - minimas[i] for i in range(7)]
    dia_max_amp = amplitudes.index(max(amplitudes)) + 1
    print(f"Mayor amplitud térmica en el día {dia_max_amp}")

def ej8():
    notas = [
        [7, 8, 6],
        [5, 6, 7],
        [9, 8, 10],
        [4, 5, 6],
        [10, 9, 8]
    ]

    print("Promedio de cada estudiante:")
    for i, fila in enumerate(notas):
        print(f"Estudiante {i+1}: {sum(fila)/len(fila):.2f}")

    print("Promedio de cada materia:")
    for j in range(3):
        materia = [notas[i][j] for i in range(5)]
        print(f"Materia {j+1}: {sum(materia)/len(materia):.2f}")

def ej9():
    tablero = [["-" for _ in range(3)] for _ in range(3)]

    def mostrar_tablero():
        for fila in tablero:
            print(" ".join(fila))

    mostrar_tablero()
    turno = "X"
    for _ in range(9):
        fila = int(input(f"Jugador {turno}, ingresá fila (0-2): "))
        col = int(input(f"Jugador {turno}, ingresá columna (0-2): "))
        if tablero[fila][col] == "-":
            tablero[fila][col] = turno
            mostrar_tablero()
            turno = "O" if turno == "X" else "X"
        else:
            print("Esa casilla ya está ocupada.")

def ej10():
    ventas = [
        [10, 15, 20, 25, 30, 18, 22],  # Producto 1
        [5, 8, 12, 7, 10, 9, 11],      # Producto 2
        [20, 25, 30, 35, 40, 32, 28],  # Producto 3
        [3, 4, 6, 5, 7, 8, 6]          # Producto 4
    ]

    print("Total vendido por producto:")
    for i, producto in enumerate(ventas):
        print(f"Producto {i+1}: {sum(producto)}")

    dias = [sum(col) for col in zip(*ventas)]
    dia_max = dias.index(max(dias)) + 1
    print(f"Día con mayores ventas: Día {dia_max}")

    totales_productos = [sum(prod) for prod in ventas]
    producto_max = totales_productos.index(max(totales_productos)) + 1
    print(f"Producto más vendido: Producto {producto_max}")

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
        print("\n=== TP5 - Hub de Ejercicios ===")
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
