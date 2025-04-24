# CALCULADORA DE PESO SEGUN IMC
# Formula: peso (kg) / altura (m) * 2

def programa():
    altura = 0
    peso = 0
    total = 0
    while True:
        print("CALCULADORA DE PESO (IMC)")
        print(f"Su altura actual es: {altura}m y su peso actual es {peso}kg\n")
        print("1. Introducir datos")
        print("2. Comprobar datos")
        print("3. Cerrar Programa\n")
        opcion = input("Porfavor, seleccione una de nuestras opciones.\n")
        if opcion == '1':
            altura = float(input("Porfavor, introduzca su altura.\n"))
            peso = float(input("Porfavor, introduzca su peso.\n"))
            print(f"¿Tiene un peso de {peso}kg y una altura de {altura}m?")
        elif opcion == '2':
            if peso == 0 or altura == 0:
                print("Error: Dato Faltante. Porfavor, ingrese los datos correctamente.\n")
            else:
                total = peso / (altura * 2)
                if total >= 18.5 and total < 24.9:
                    print("Se encuentra adentro del rango de peso normal.\n")
                elif(total >= 25 and total < 29.9):
                    print("Se encuentra adentro del rango de sobrepeso.\n")
                elif total >= 30:
                    print("Se encuentra adentro del rango de obesidad.\n")
                elif total < 18.5:
                    print("Se encuentra adentro del rango de desnutricion.\n")
        elif opcion == '3':
            break
        else:
            print("ERROR: Introduce un opcion valida.\n")

if __name__ == "__main__":
    programa()
