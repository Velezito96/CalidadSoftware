import os
import pytest
from colorama import init, Fore, Style

# Inicializar colorama
init(autoreset=True)

def limpiar_pantalla():
    # Función para limpiar la pantalla en Windows
    os.system('cls')

def sumar(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Error: Debe ingresar números válidos")
    return num1 + num2

def restar(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Error: Debe ingresar números válidos")
    return num1 - num2

def multiplicar(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Error: Debe ingresar números válidos")
    return num1 * num2

def dividir(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Error: Debe ingresar números válidos")
    if num2 == 0:
        raise ValueError(" No se puede dividir entre cero")
    if num1 < 0 or num2 < 0:
        raise ValueError("Error: No se permiten números negativos")
    return num1 / num2

def calculadora():
    """
    Calculadora simple en Python
    """
    while True:  # Bucle principal para repetir la ejecución
        limpiar_pantalla()  # Limpia la pantalla antes de mostrar el menú

        # Encabezado centrado y en color verde brillante
        encabezado = "Calculadora Simple"
        print(Fore.GREEN + Style.BRIGHT + "{:^80}".format(encabezado))
        print(Fore.GREEN + "-" * 80)

        # Menú de opciones con colores
        opciones = [
            (Fore.CYAN + "1. Suma"),
            (Fore.CYAN + "2. Resta"),
            (Fore.CYAN + "3. Multiplicación"),
            (Fore.CYAN + "4. División"),
            (Fore.RED + "5. Salir")
        ]
        for opcion in opciones:
            print("{:^80}".format(opcion))
        print("-" * 80)

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                resultado = sumar(num1, num2)
                print(Fore.YELLOW + f"\nLa suma de {num1} y {num2} es: {resultado}\n")
            except ValueError as e:
                print(Fore.RED + f"\nError: {e}\n")
        elif opcion == '2':
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                resultado = restar(num1, num2)
                print(Fore.YELLOW + f"\nLa resta de {num1} y {num2} es: {resultado}\n")
            except ValueError as e:
                print(Fore.RED + f"\nError: {e}\n")
        elif opcion == '3':
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                resultado = multiplicar(num1, num2)
                print(Fore.YELLOW + f"\nLa multiplicación de {num1} y {num2} es: {resultado}\n")
            except ValueError as e:
                print(Fore.RED + f"\nError: {e}\n")
        elif opcion == '4':
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                resultado = dividir(num1, num2)
                print(Fore.YELLOW + f"\nLa división de {num1} entre {num2} es: {resultado}\n")
            except ValueError as e:
                print(Fore.RED + f"\nError: {e}\n")
        elif opcion == '5':
            print(Fore.RED + "Saliendo de la calculadora...")
            break  # Salir del bucle y terminar el programa
        else:
            print(Fore.RED + "Opción no válida. Por favor, seleccione una opción válida.")

        input(Fore.MAGENTA + "Presione Enter para continuar...")

# Llamamos a la función calculadora cuando se ejecute el script
if __name__ == "__main__":
    calculadora()
