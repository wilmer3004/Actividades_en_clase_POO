from Vehiculo import Vehiculo
class Carro(Vehiculo):
    # Metodo constructor
    def __init__(self, placa, nombre, marca, modelo, color, num_puertas,cobro_peaje):
        super().__init__(placa, nombre, marca, modelo, color, cobro_peaje)
        self.num_puertas = num_puertas
      
      
    # Metodo para calcular el peaje
    def calcular_peaje(self, cobro_peaje_carro):
        self.cobro_peaje = cobro_peaje_carro
    
    # Metodo para mostrar la informacion del carro
    def __str__(self):
        return self.info_vehiculo() + f", Numero de puertas: {self.num_puertas}"