class Nodo:
    def __init__(self,anterior,siguiente,nombre,apellido,telefono):
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def getTelefono(self):
        return self.telefono
    def getAnterior(self):
        return self.anterior
    def getSiguiente(self):
        return self.siguiente

    def setNombre(self,nombre):
        self.nombre=nombre
    def setApellido(self, apellido):
        self.apellido=apellido
    def setTelefono(self,telefono):
        self.telefono=telefono

    def setAnterior(self, anterior):
        self.anterior = anterior
    def setSiguiente(self, siguiente):
        self.siguiente=siguiente

