class Vehiculo:
    def __init__(self,fecha_fabricacion,vin_chasis,vin_motor):
        self.fecha_fabricacion=fecha_fabricacion
        self.vin_chasis=vin_chasis
        self.vin_motor=vin_motor
        
    def obtener_atr(self):
        return f"fecha de fabricacion: {self.fecha_fabricacion}, chasis: {self.vin_chasis}, motor: {self.vin_motor}"

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, precio, fecha_fabricacion, vin_chasis, vin_motor):
        super().__init__(fecha_fabricacion,vin_chasis,vin_motor)
        self.marca=marca
        self.modelo=modelo
        self.precio=precio
        
    def obt_datos(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Precio: {self.precio}"
        
    def mensaje_personalizado(self): 
        return f"La marca del auto es {self.marca}, modelo {self.modelo} y costo {self.precio}. La fecha de fabricacion de este es {self.fecha_fabricacion} y su motor y chasis son respectivamente {self.vin_motor}, {self.vin_chasis}"
    
auto_1 = Automovil("Renault", "2008", 16000000, "twingo",)
print(auto_1.mensaje_personalizado())