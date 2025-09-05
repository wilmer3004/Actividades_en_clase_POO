from Vehiculo import Vehiculo
class Moto(Vehiculo):
    # Metodo constructor
    def __init__(self, placa, nombre, marca, modelo, color, cilindraje,cobro_peaje):
        super().__init__(placa, nombre, marca, modelo, color, cobro_peaje)
        self.cilindraje = cilindraje
      
      
    # Metodo para calcular el peaje
    def calcular_peaje(self, cobro_peaje_moto):
        self.cobro_peaje = cobro_peaje_moto
    
    # Metodo para mostrar la informacion de la moto
    def __str__(self):
        return self.info_vehiculo() + f", Cilindraje: {self.cilindraje}"