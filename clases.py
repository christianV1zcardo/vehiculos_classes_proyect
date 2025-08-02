class Vehiculo:
    
    cantidad_vehiculos_creados = 0

    @classmethod
    def mostrar_total_vehiculos_creados(cls):
        print(f"Se han creado {cls.cantidad_vehiculos_creados} vehículos")
   
    def __init__(self, marca: str, modelo: str, year: int, 
                 asignado: bool =False ):
        self.marca = marca
        self.modelo = modelo
        self.year = year
        self.asignado = asignado
        
        self.velocidad_actual: float = 0.0
        self.encendido: bool = False
        self.kilometraje = 0
        
        Vehiculo.cantidad_vehiculos_creados += 1
        
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
        if self.encendido:
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
            
    def recorrer_distancia(self, distancia):
        if distancia > 0 and isinstance(distancia, int) and self.encendido:
            self.kilometraje += distancia
            print(f"Se recorrieron {distancia} kilómetros")    
        else:
            print(f"La distancia debe ser un int positivo")
            
    def mostrar_estado(self):
        print(f"- Marca: {self.marca}\n"
            f"- Modelo: {self.modelo}\n"
            f"- Año: {self.year}\n"
            f"- Asignado: {self.asignado}\n"
            f"- Encendido: {self.encendido}\n"
            f"- Kilometraje: {self.kilometraje}\n"
            f"- Velocidad Actual: {self.velocidad_actual}")       
            
            
class Automovil(Vehiculo):
    def __init__(self, marca: str, modelo: str, year: int, n_puertas: int, 
                 asignado=False):
        super().__init__(marca, modelo, year, asignado)
        self.n_puertas = n_puertas
    
    def tocar_bocina(self):
        print("BEEEEEP BEEEEP")
        
    def mostrar_estado(self):
        print(f"Vehículo: {type(self).__name__}\n"
            f"- Marca: {self.marca}\n"
            f"- Modelo: {self.modelo}\n"
            f"- Año: {self.year}\n"
            f"- Asignado: {self.asignado}\n"
            f"- Encendido: {self.encendido}\n"
            f"- Kilometraje: {self.kilometraje}\n"
            f"- Velocidad Actual: {self.velocidad_actual}\n"
            f"- Número de Puertas: {self.n_puertas}")       
        

class Motocicleta(Vehiculo):
    def __init__(self, marca: str, modelo: str, year: int, es_deportiva: bool,
                 asignado=False):
        super().__init__(marca, modelo, year, asignado)
        self.es_deportiva = es_deportiva
        
    def hacer_caballito(self):
        if self.encendido == True and self.velocidad_actual > 30:
            print("*Hace caballito*")
        else:
            print("No se puede hacer caballito")
    
    def mostrar_estado(self):
        print(f"Vehículo: {type(self).__name__}\n"
            f"- Marca: {self.marca}\n"
            f"- Modelo: {self.modelo}\n"
            f"- Año: {self.year}\n"
            f"- Asignado: {self.asignado}\n"
            f"- Encendido: {self.encendido}\n"
            f"- Kilometraje: {self.kilometraje}\n"
            f"- Velocidad Actual: {self.velocidad_actual}\n"
            f"- Es Deportiva: {self.es_deportiva}") 
            
        
class Camion(Vehiculo):
    def __init__(self, marca: str, modelo: str, year: int, 
                 capacidad_carga_kg: float, asignado=False):
        super().__init__(marca, modelo, year, asignado)
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
            
    def mostrar_estado(self):
        print(f"Vehículo: {type(self).__name__}\n"
            f"- Marca: {self.marca}\n"
            f"- Modelo: {self.modelo}\n"
            f"- Año: {self.year}\n"
            f"- Asignado: {self.asignado}\n"
            f"- Encendido: {self.encendido}\n"
            f"- Kilometraje: {self.kilometraje}\n"
            f"- Velocidad Actual: {self.velocidad_actual}\n"
            f"- Capacidad de carga: {self.capacidad_carga_kg}\n"
            f"- Carga Actual: {self.carga_actual_kg}") 


class Flota:
    def __init__(self, vehiculos: list):
        self.vehiculos = vehiculos
        
    def agregar_vehiculo(self, vehiculo):
        if isinstance(vehiculo, Vehiculo):
            self.vehiculos.append(vehiculo)
            print(f"{vehiculo} añadido correctamente a la lista")
        else:
            raise TypeError(f"{vehiculo} no es un heredero de Vehiculo")
    
    def remover_vehiculo(self, vehiculo):
        if vehiculo in self.vehiculos:
            self.vehiculos.remove(vehiculo)
            print(f"{vehiculo} eliminado de la lista correctamente")
        else:
            print(f"{vehiculo} no existe en la lista")
            
    def mostrar_estado_flota(self):
        for vehiculo in self.vehiculos:
            vehiculo.mostrar_estado()
            print("------------------------------")
            
    def contar_vehiculos(self, tipo_vehiculo: str=None):
        if tipo_vehiculo == None:
            print(len(self.vehiculos))
        else:
            tipos = []
            for tipo in self.vehiculos:
                tipo = type(tipo).__name__
                tipos.append(tipo)
                
            print(tipos.count(tipo_vehiculo))
            

class Conductor:
    def __init__(self):
        self.vehiculo_asignado = ""
    
    def asignar_vehiculo(self, vehiculo):
        if isinstance(vehiculo, Vehiculo):
            vehiculo.asignado = True
            self.vehiculo_asignado = vehiculo
            print(f"{vehiculo} asignado correctamente")
        else:
            raise TypeError(f"{vehiculo} debe ser un Vehiculo")
    
    def conducir(self, cantidad, distancia):
        if self.vehiculo_asignado:
            self.vehiculo_asignado.encender()
            self.vehiculo_asignado.acelerar(cantidad)
            self.vehiculo_asignado.recorrer_distancia(distancia)
        
        else:
            print("El conductor no tiene un vehículo asignado")
            
    def frenar(self, cantidad):
        self.vehiculo_asignado.frenar(cantidad)