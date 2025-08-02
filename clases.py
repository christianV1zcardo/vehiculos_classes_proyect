class Vehiculo:
    def __init__(self, marca: str, modelo: str, year: int):
        self.marca = marca
        self.modelo = modelo
        self.year = year
        
        self.velocidad_actual: float = 0.0
        self.encendido: bool = False
        
    def encender(self):
        self.encendido = True
        print("BBRRRRRMMMM - Vehículo encendido")
        
    def apagar(self):
        self.encendido = False
        self.velocidad_actual = 0.0
        print("*Silencio* - Vehículo apagado")

    def acelerar(self, cantidad):
        if cantidad < 0:
            raise ValueError("Cantidad debe ser positivo")        
        if self.encendido == True:
            self.velocidad_actual += cantidad
            print("bbbrrrmm")
        else:
            print("No se puede acelerar, vehículo apagado")
        
    def frenar(self, cantidad):
        if cantidad < 0:
            raise ValueError("Cantidad debe ser positivo")
        if cantidad < self.velocidad_actual:
            self.velocidad_actual -= cantidad
        else:
            self.velocidad_actual = 0.0
    
    
class Automovil(Vehiculo):
    def __init__(self, marca: str, modelo: str, year: int, n_puertas: int):
        super().__init__(marca, modelo, year)
        self.n_puertas = n_puertas
    
    def tocar_bocina(self):
        print("BEEEEEP BEEEEP")
        

class Motocicleta(Vehiculo):
    def __init__(self, marca: str, modelo: str, year: int, es_deportiva: bool):
        super().__init__(marca, modelo, year)
        self.es_deportiva = es_deportiva
        
    def hacer_caballito(self):
        if self.encendido == True and self.velocidad_actual > 30:
            print("*Hace caballito*")
        else:
            print("No se puede hacer caballito")
        
        
class Camion(Vehiculo):
    def __init__(self, marca: str, modelo: str, year: int, capacidad_carga_kg: float):
        super().__init__(marca, modelo, year)
        self.capacidad_carga_kg = capacidad_carga_kg
        
        self.carga_actual_kg: float = 0.0
        
    def cargar(self, peso):
        if self.carga_actual_kg + peso <= self.capacidad_carga_kg:
            self.carga_actual_kg += peso
            print(f"Añadidos {peso} kg de peso")
        else:
            print("Añadir este peso supera la carga máxima del camión")
    
    def descargar(self, peso):
        if self.carga_actual_kg - peso >= 0:
            self.carga_actual_kg -= peso
            print(f"Se restaron {peso} kg de peso")
        
        else:
            print(f"No se puede restar más peso del que hay en el camión")
            
    def acelerar(self, cantidad):
        if cantidad < 0:
            raise ValueError("Cantidad debe ser positivo") 
        
        mitad_capacidad = self.capacidad_carga_kg * 0.5
        if self.carga_actual_kg > mitad_capacidad:
            mitad_aceleracion = cantidad / 2
            self.velocidad_actual += mitad_aceleracion
            print("bbrrmm - Se acelera a medias")
        else:
            self.velocidad_actual += cantidad
            print("bbbbrrrrmmmm - Se acelera normalmente")