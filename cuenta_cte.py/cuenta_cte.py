class cuenta_cte:
    def __init__(self, name="", birthdate="", Document="", telephone="", gmail="", initial_balance=0):
        self.__saldo = initial_balance
        self.__titular = name
        self.__fecha_nacimiento = birthdate
        self.__Documento = Document
        self.__telefono = telephone
        self.__correo = gmail

    def depositar(self, cantidad):
        self.__saldo += cantidad
        print(f"Depósito: {cantidad}. Saldo actual: {self.__saldo}")

    def retirar(self, cantidad):
        if cantidad > self.__saldo:
            print("Fondos insuficientes.")
        else:
            self.__saldo -= cantidad
            print(f"Retiro: {cantidad}. Saldo actual: {self.__saldo}")

    def obtener_saldo(self):
        return self.__saldo

    def __str__(self):
        return f"Cuenta corriente con saldo: {self.__saldo}"

    def __nombre__(self):
        return self.__titular
    def __fecha_nacimiento__(self):
        return self.__fecha_nacimiento
    def __Documento__(self):
        return self.__Documento
    def __telefono__(self):
        return self.__telefono
    def __correo__(self):
        return self.__correo

    def __set_name__(self, name):
        self.__titular = name
    def __set_fecha_nacimiento__(self, birthdate):
        self.__fecha_nacimiento = birthdate
    def __set_Documento__(self, Document):
        self.__Documento = Document
    def __set_telefono__(self, telephone):
        self.__telefono = telephone
    def __set_correo__(self, gmail):
        self.__correo = gmail

    def __get_name__(self):
        return self.__titular
    def __get_fecha_nacimiento__(self):
        return self.__fecha_nacimiento
    def __get_Documento__(self):
        return self.__Documento
    def __get_telefono__(self):
        return self.__telefono
    def __get_correo__(self):
        return self.__correo
