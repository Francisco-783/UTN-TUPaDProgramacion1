import random
from statistics import mean, median, mode

# ------------------------------
# Definición de funciones (TP3)
# ------------------------------

def ej1():
    edad = int(input("Ingresá tu edad: "))
    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")

def ej2():
    nota = float(input("Ingresá tu nota: "))
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")

def ej3():
    num = int(input("Ingresá un número par: "))
    if num % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")

def ej4():
    edad = int(input("Ingresá tu edad: "))
    if edad < 12:
        print("Niño/a")
    elif edad < 18:
        print("Adolescente")
    elif edad < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")

def ej5():
    contraseña = input("Ingresá una contraseña (8 a 14 caracteres): ")
    if 8 <= len(contraseña) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

def ej6():
    numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
    media = mean(numeros_aleatorios)
    mediana = median(numeros_aleatorios)
    moda = mode(numeros_aleatorios)

    print(f"Media: {media:.2f}, Mediana: {mediana}, Moda: {moda}")

    if media > mediana > moda:
        print("Sesgo positivo (a la derecha)")
    elif media < mediana < moda:
        print("Sesgo negativo (a la izquierda)")
    elif media == mediana == moda:
        print("Sin sesgo")
    else:
        print("Distribución irregular")

def ej7():
    texto = input("Ingresá una palabra o frase: ")
    if texto[-1].lower() in "aeiou":
        print(texto + "!")
    else:
        print(texto)

def ej8():
    nombre = input("Ingresá tu nombre: ")
    opcion = input("Elegí una opción (1=mayúsculas, 2=minúsculas, 3=capitalizar): ")

    if opcion == "1":
        print(nombre.upper())
    elif opcion == "2":
        print(nombre.lower())
    elif opcion == "3":
        print(nombre.title())
    else:
        print("Opción inválida")

def ej9():
    magnitud = float(input("Ingresá la magnitud del terremoto: "))
    if magnitud < 3:
        print("Muy leve (imperceptible)")
    elif magnitud < 4:
        print("Leve (ligeramente perceptible)")
    elif magnitud < 5:
        print("Moderado (sentido por personas, pero no causa daños)")
    elif magnitud < 6:
        print("Fuerte (puede causar daños en estructuras débiles)")
    elif magnitud < 7:
        print("Muy fuerte (puede causar daños significativos)")
    else:
        print("Extremo (graves daños a gran escala)")

def ej10():
    hemisferio = input("Ingresá tu hemisferio (N/S): ").upper()
    mes = int(input("Ingresá el número de mes (1-12): "))
    dia = int(input("Ingresá el día: "))

    # Convertimos mes y día a un "día del año" simplificado
    meses_dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dia_del_año = sum(meses_dias[:mes-1]) + dia

    if 355 <= dia_del_año or dia_del_año <= 79:  # 21 dic - 20 mar
        estacion = "Invierno" if hemisferio == "N" else "Verano"
    elif 80 <= dia_del_año <= 171:  # 21 mar - 20 jun
        estacion = "Primavera" if hemisferio == "N" else "Otoño"
    elif 172 <= dia_del_año <= 263:  # 21 jun - 20 sep
        estacion = "Verano" if hemisferio == "N" else "Invierno"
    else:  # 21 sep - 20 dic
        estacion = "Otoño" if hemisferio == "N" else "Primavera"

    print(f"Estación: {estacion}")

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
        print("\n=== TP3 - Hub de Ejercicios ===")
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
