class Vehiculo:
    # Metodo constructor
    def __init__(self, placa, nombre, marca, modelo, color, cobro_peaje):
        self.placa = placa
        self.nombre = nombre
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.cobro_peaje = cobro_peaje
        
    # Metodo para calcular el peaje
    
    def calcular_peaje(self, cobro_peaje):
        self.cobro_peaje = cobro_peaje
        return self.cobro_peaje
    
    def info_vehiculo(self):
        return f"Placa: {self.placa}, Nombre: {self.nombre}, Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Cobro peaje$: {self.cobro_peaje}"
