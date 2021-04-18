
from nodo import Nodo

generador_grafo = ""

class Lista_Doblemente_Enlazada:

    def __init__(self):
        self.insertar_inicio=self.insertar_final=None
        
    def insertar(self,nombre,apellido,telefono):
        if self.insertar_inicio==None:
            self.insertar_inicio=self.insertar_final=Nodo(None,None,nombre,apellido,telefono)
        else:
            temp=self.insertar_inicio
            temp_insertar=False
            nuevo_nodo=Nodo(temp,temp.getSiguiente(),nombre,apellido,telefono)
            if is not temp_insertar:
                nuevo_nodo=Nodo(None,self.insertar_final,nombre,apellido,telefono)
                self.insertar_final.setAnterior(nuevo_nodo)
                self.insertar_final=nuevo_nodo
    
 