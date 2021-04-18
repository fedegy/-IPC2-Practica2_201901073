from nodo import Nodo
import os

class Lista_Doblemente_Enlazada:
    generador_grafo=""
    def __init__(self):
        self.insertar_inicio=self.insertar_final=None
    def insertar(self, nombre,apellido,telefono):
        if self.insertar_inicio==None:
            self.insertar_inicio=self.insertar_final=Nodo(None,None,nombre,apellido,telefono)
        else:
            temp_insertar=False
            if not temp_insertar:
                nodo_nuevo=Nodo(None,self.insertar_final,nombre,apellido,telefono)
                self.insertar_final.setAnterior(nodo_nuevo)
                self.insertar_final=nodo_nuevo

    def generar_grafoContactos(self):
        global generador_grafo
        generador_grafo="digraph Contactos{\nnode [shape=\"box\"]\n"
        self.grafo_temp()
        generador_grafo+="}"
        grafo(generador_grafo)

    def grafo_temp(self):
        global generador_grafo
        if not self.insertar_inicio==None:
            temp=self.insertar_final
            while temp!=None:
                if temp==self.insertar_inicio:
                    generador_grafo+="\""+str(temp)+"\"[label=\""+"Nombre: "+str(temp.nombre)+"\n Apellido: "+str(temp.apellido)+ "\n Telefono: "+ str(temp.telefono)+"\"]\n"
                elif temp==self.insertar_final:
                    generador_grafo+="\""+str(temp)+"\"[label=\""+"Nombre: "+str(temp.nombre)+"\n Apellido: "+str(temp.apellido)+ "\n Telefono: "+ str(temp.telefono)+"\"]\n"
                else:
                    generador_grafo+="\""+str(temp)+"\"[label=\""+"Nombre: "+str(temp.nombre)+"\n Apellido: "+str(temp.apellido)+"\n Telefono: "+str(temp.telefono)+"\"]\n"     
                if temp.getAnterior()!=None:
                    generador_grafo+= "\""+str(temp)+"\"->\""+str(temp.getAnterior())+"\"\n"
                if temp.getSiguiente() != None:
                    generador_grafo+="\""+str(temp)+"\"->\""+str(temp.getSiguiente())+"\"\n" 
                temp=temp.getSiguiente()
    
    def buscar(self,telefono):
        temp=self.insertar_inicio=self.insertar_final
        if temp.getTelefono()==telefono:
            print("Nombre: "+str(temp.nombre))
            print("Apellido: "+str(temp.apellido))
            print("Telefono: "+str(temp.telefono))

def grafo(generador):
    file=open('grafo_contactos.dot','w')
    file.write(generador)
    file.close()
    os.system('dot -Tpng grafo_contactos.dot -o grafo_contactos.png')
    os.startfile('grafo_contactos.png')