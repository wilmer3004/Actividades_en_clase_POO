from Camion import Camion
from Moto import Moto
from Carro import Carro

def main():
    vehiculos = []  # lista para polimorfismo

# Menu de opciones
    while True:
        print("Seleccione el tipo de vehiculo:")
        print("""----------------------------------------------------
1. Carro
2. Moto
3. Camion
4. Mostrar todos los vehículos y peajes
5. Salir""")
        opcion = input("Ingrese una opcion (1-5): ")
        print("----------------------------------------------------")   

# Procesar la opcion seleccionada
        if opcion == '1':
            placa = input("Ingrese la placa del carro: ")
            nombre = input("Ingrese el nombre del carro: ")
            marca = input("Ingrese la marca del carro: ")
            modelo = input("Ingrese el modelo del carro: ")
            color = input("Ingrese el color del carro: ")
            num_puertas = input("Ingrese el numero de puertas del carro: ")
            carro = Carro(placa, nombre, marca, modelo, color, num_puertas)
            vehiculos.append(carro)
            print("Carro agregado con éxito.")

        elif opcion == '2':
            placa = input("Ingrese la placa de la moto: ")
            nombre = input("Ingrese el nombre de la moto: ")
            marca = input("Ingrese la marca de la moto: ")
            modelo = input("Ingrese el modelo de la moto: ")
            color = input("Ingrese el color de la moto: ")
            cilindraje = input("Ingrese el cilindraje de la moto: ")
            moto = Moto(placa, nombre, marca, modelo, color, cilindraje)
            vehiculos.append(moto)
            print("Moto agregada con éxito.")

        elif opcion == '3':
            placa = input("Ingrese la placa del camion: ")
            nombre = input("Ingrese el nombre del camion: ")
            marca = input("Ingrese la marca del camion: ")
            modelo = input("Ingrese el modelo del camion: ")
            color = input("Ingrese el color del camion: ")
            num_ejes = input("Ingrese el numero de ejes del camion: ")
            camion = Camion(placa, nombre, marca, modelo, color, num_ejes)
            vehiculos.append(camion)
            print("Camion agregado con éxito.")

        elif opcion == '4':
            print("===== LISTA DE VEHÍCULOS Y SUS PEAJES =====")
            for v in vehiculos:
                print(v)
            print("==========================================")

        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

    print("""
--------------------------------------------------
Fin del programa
--------------------------------------------------    
          """)

main()
