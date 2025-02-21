from datetime import datetime

class Cliente:
    def __init__(self, cedula, nombre, apellido, telefono, correo, direccion, fecha_nacimiento):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento
    

    def obtener_datos(self):
        return f"Cédula: {self.cedula}, Nombre: {self.nombre}, Apellido: {self.apellido}, Teléfono: {self.telefono}, Correo: {self.correo}, Dirección: {self.direccion}, Fecha de nacimiento: {self.fecha_nacimiento}"
    

    def calcular_edad(self):
        fecha_nacimiento = datetime.strptime(self.fecha_nacimiento, "%Y/%m/%d")
        hoy = datetime.today()
        edad = hoy.year - fecha_nacimiento.year
        if hoy.month < fecha_nacimiento.month or (hoy.month == fecha_nacimiento.month and hoy.day < fecha_nacimiento.day):
            edad -= 1
        return edad


cliente1 = Cliente(
    cedula="1003237964",
    nombre="pedro",
    apellido="moreno",
    telefono="3106537911",
    correo="itspedrolouis@gmail.com",
    direccion="13 de junio",
    fecha_nacimiento="02/06/2001"
)


edad_cliente = cliente1.calcular_edad()
print(f"Mi nombre es {cliente1.nombre} {cliente1.apellido} y vivo en {cliente1.direccion} y tengo {edad_cliente} años de edad.")
