from Vehiculo import Vehiculo

class Camion(Vehiculo):
    # Metodo constructor
    def __init__(self, placa, nombre, marca, modelo, color, num_ejes,cobro_peaje):
        super().__init__(placa, nombre, marca, modelo, color, cobro_peaje)
        self.num_ejes = num_ejes
      
      
    # Metodo para calcular el peaje
    def calcular_peaje(self, cobro_peaje_camion):
        self.cobro_peaje = cobro_peaje_camion
    
    # Metodo para mostrar la informacion del camion
    def __str__(self):
        return self.info_vehiculo() + f", Numero de ejes: {self.num_ejes}"